import asyncio
import inspect
import json
import websockets
from websockets.exceptions import (
    ConnectionClosedError,
    ConnectionClosedOK,
    WebSocketException,
)
from orderly_evm_connector.lib.utils import orderlyLog, parse_proxies, decode_ws_error_code
from orderly_evm_connector.lib.constants import (
    WEBSOCKET_TIMEOUT_IN_SECONDS,
    WEBSOCKET_FAILED_MAX_RETRIES,
    WEBSOCKET_RETRY_SLEEP_TIME,
)

class AsyncWebsocketManager:
    def __init__(
        self,
        websocket_url,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
        on_ping=None,
        on_pong=None,
        timeout=WEBSOCKET_TIMEOUT_IN_SECONDS,
        debug=False,
        proxies=None,
        max_retries=WEBSOCKET_FAILED_MAX_RETRIES,
    ):
        self.websocket_url = websocket_url
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.init = False
        self.on_error = on_error
        self.on_ping = on_ping
        self.on_pong = on_pong
        self.timeout = timeout
        self.logger = orderlyLog(debug=debug)
        self._proxy_params = parse_proxies(proxies) if proxies else {}
        self.subscriptions = []
        self._login = False
        self.max_retries = max_retries
        self.ws = None
        self.loop = asyncio.get_event_loop()
        self._stopping = False
        self._on_close_called = False

    def start(self):
        pass

    async def create_ws_connection(self):
        retries = 0
        while retries <= self.max_retries:
            try:
                self.logger.debug(
                    f"Creating connection with WebSocket Server: {self.websocket_url}, proxies: {self._proxy_params}"
                )
                self.ws = await websockets.connect(
                    self.websocket_url, timeout=self.timeout, **self._proxy_params
                )
                self.logger.debug(
                    f"WebSocket connection has been established: {self.websocket_url}, proxies: {self._proxy_params}"
                )
                self._stopping = False
                self._on_close_called = False
                self.init = False
                if self.on_open:
                    await self._callback(self.on_open)
                return
            except Exception as e:
                self.logger.error(f"Failed to create WebSocket connection: {e}")
                retries += 1
                if retries <= self.max_retries:
                    self.logger.warning(
                        f"Retrying connection... (Attempt {retries}/{self.max_retries})"
                    )
                    await asyncio.sleep(WEBSOCKET_RETRY_SLEEP_TIME)
                else:
                    raise

    async def reconnect(self):
        if self._stopping:
            return
        self.logger.warning("Reconnecting to WebSocket...")
        await self._internal_close()
        self._login = False
        await self.create_ws_connection()

    def send_message(self, message):
        self.logger.debug("Sending message to Orderly WebSocket Server: %s", message)
        if self.ws and not self.ws.closed and not self._stopping:
            asyncio.create_task(self.ws.send(message))
        else:
            self.logger.debug("Skipping send_message because websocket is not connected.")

    async def run(self):
        await self.create_ws_connection()
        await self.read_data()

    async def ensure_init(self):
        while not self._stopping:
            if self.init:
                break
            await asyncio.sleep(1)

    async def _handle_heartbeat(self):
        try:
            _payload = {"event": "pong"}
            if self.ws and not self.ws.closed:
                await self.ws.send(json.dumps(_payload))
                self.logger.debug(f"Sent Ping frame: {_payload}")
        except Exception as e:
            self.logger.error("Failed to send Ping: {}".format(e))

    async def read_data(self):
        while True:
            if self._stopping:
                await self._notify_close()
                break
            try:
                ws = self.ws
                if ws is None:
                    await asyncio.sleep(WEBSOCKET_RETRY_SLEEP_TIME)
                    continue
                message = await ws.recv()
                self.init = True
            except (ConnectionClosedError, ConnectionClosedOK) as e:
                close_code = getattr(e, "code", None)
                close_reason = getattr(e, "reason", "")
                if self._stopping:
                    self.logger.info("WebSocket connection closed by client.")
                    await self._notify_close()
                    break
                if close_code == 1000:
                    self.logger.info("WebSocket connection closed normally (code 1000).")
                else:
                    self.logger.warning(
                        f"WebSocket connection closed (code={close_code}, reason={close_reason})."
                    )
                await self._notify_close()
                await self.reconnect()
                continue
            except WebSocketException as e:
                if self._stopping:
                    break
                self.logger.error(f"WebSocket exception: {e}")
                await self._notify_close()
                await self.reconnect()
                continue
            except Exception as e:
                if self._stopping:
                    break
                self.logger.error(f"Exception in read_data: {e}")
                await self._notify_close()
                await self.reconnect()
                continue

            payload = b""
            try:
                payload = message
                if isinstance(message, str):
                    payload = message.encode()
                elif isinstance(message, (bytearray, memoryview)):
                    payload = bytes(message)
                _message = json.loads(message)
            except json.JSONDecodeError:
                err_code = decode_ws_error_code(payload)
                if err_code == "1000":
                    self.logger.info("Websocket closed normally (code 1000).")
                    if self._stopping:
                        await self._notify_close()
                        break
                elif err_code:
                    self.logger.warning(
                        f"Websocket error code received: {err_code}"
                    )
                continue

            if "event" in _message and _message["event"] == "ping":
                await self._handle_heartbeat()
            else:
                await self._callback(self.on_message, _message)

    async def close(self):
        self._stopping = True
        await self._internal_close()

    async def _callback(self, callback, *args):
        if callback:
            try:
                result = callback(self, *args)
                if inspect.isawaitable(result):
                    await result
            except Exception as e:
                self.logger.error("Error from callback {}: {}".format(callback, e))
                if self.on_error and callback is not self.on_error:
                    await self._callback(self.on_error, e)

    async def _notify_close(self):
        if not self._on_close_called:
            self._on_close_called = True
            await self._callback(self.on_close)

    async def _internal_close(self):
        if self.ws and not self.ws.closed:
            await self.ws.close()
        self.ws = None
        self.init = False
        self._login = False
