import asyncio
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
                if self.on_open:
                    self.on_open(self)
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
        self.logger.warning("Reconnecting to WebSocket...")
        await self.close()
        await self.create_ws_connection()

    def send_message(self, message):
        self.logger.debug("Sending message to Orderly WebSocket Server: %s", message)
        asyncio.create_task(self.ws.send(message))

    async def run(self):
        await self.create_ws_connection()
        await self.read_data()

    async def ensure_init(self):
        while True:
            if self.init:
                break
            await asyncio.sleep(1)

    async def _handle_heartbeat(self):
        try:
            _payload = {"event": "pong"}
            await self.ws.send(json.dumps(_payload))
            self.logger.debug(f"Sent Ping frame: {_payload}")
        except Exception as e:
            self.logger.error("Failed to send Ping: {}".format(e))

    async def read_data(self):
        try:
            while True:
                try:
                    message = await self.ws.recv()
                    _message = json.loads(message)
                    self.init = True
                except json.JSONDecodeError:
                    err_code = decode_ws_error_code(message)
                    self.logger.warning(f"Websocket error code received: {err_code}")
                else:
                    if "event" in _message and _message["event"] == "ping":
                        await self._handle_heartbeat()
                    else:
                        await self._callback(self.on_message, _message)
        except (ConnectionClosedError, ConnectionClosedOK):
            self.logger.warning("WebSocket connection closed. Reconnecting...")
            await self.reconnect()
        except WebSocketException as e:
            self.logger.error(f"WebSocket exception: {e}")
            await self.reconnect()
        except Exception as e:
            self.logger.error(f"Exception in read_data: {e}")
            await self.reconnect()

    async def close(self):
        if self.ws and not self.ws.closed:
            await self.ws.close()

    async def _callback(self, callback, *args):
        if callback:
            try:
                await callback(self, *args)
            except Exception as e:
                self.logger.error("Error from callback {}: {}".format(callback, e))
                if self.on_error:
                    await self.on_error(self, e)
