import threading
import json
import time
from websocket import (
    create_connection,
    ABNF,
    WebSocketException,
    WebSocketConnectionClosedException,
    WebSocketTimeoutException,
)
from orderly_evm_connector.lib.utils import orderlyLog, parse_proxies, decode_ws_error_code
from orderly_evm_connector.lib.constants import (
    WEBSOCKET_TIMEOUT_IN_SECONDS,
    WEBSOCKET_FAILED_MAX_RETRIES,
    WEBSOCKET_RETRY_SLEEP_TIME,
)


class OrderlySocketManager(threading.Thread):
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
        threading.Thread.__init__(self)
        self.websocket_url = websocket_url
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.on_error = on_error
        self.on_ping = on_ping
        self.on_pong = on_pong
        self.timeout = timeout
        self.logger = orderlyLog(debug=debug)
        self._proxy_params = parse_proxies(proxies) if proxies else {}
        self.subscriptions = []
        self._login = False
        self.create_ws_connection()

    def create_ws_connection(self):
        retries = 0
        while retries <= WEBSOCKET_FAILED_MAX_RETRIES:
            try:
                self.logger.debug(
                    f"Creating connection with WebSocket Server: {self.websocket_url}, proxies: {self._proxy_params}"
                )
                self.ws = create_connection(
                    self.websocket_url, timeout=self.timeout, **self._proxy_params
                )
                self.logger.debug(
                    f"WebSocket connection has been established: {self.websocket_url}, proxies: {self._proxy_params}"
                )
                self.on_open(self)
                break
            except Exception as e:
                self.logger.error(f"Failed to create WebSocket connection: {e}")
                retries += 1
                if retries <= WEBSOCKET_FAILED_MAX_RETRIES:
                    self.logger.warning(
                        f"Retrying connection... (Attempt {retries}/{WEBSOCKET_FAILED_MAX_RETRIES})"
                    )
                    time.sleep(WEBSOCKET_RETRY_SLEEP_TIME)
                else:
                    raise

    def reconnect(self):
        retries = 0
        while retries <= WEBSOCKET_FAILED_MAX_RETRIES:
            try:
                self.create_ws_connection()
                self._login = False
                break
            except Exception as e:
                self.logger.error(f"Failed to reconnect: {e}")
                retries += 1
                if retries <= WEBSOCKET_FAILED_MAX_RETRIES:
                    self.logger.warning(
                        f"Retrying connection... (Attempt {retries}/{WEBSOCKET_FAILED_MAX_RETRIES})"
                    )
                    time.sleep(WEBSOCKET_RETRY_SLEEP_TIME)
                else:
                    raise

    def send_message(self, message):
        self.logger.debug("Sending message to Orderly WebSocket Server: %s", message)
        self.ws.send(message)

    def run(self):
        self.read_data()

    def _handle_heartbeat(self):
        try:
            _payload = {"event": "pong"}
            self.ws.send(json.dumps(_payload))
            self.logger.debug(f"Sent Ping frame:{_payload}")
        except Exception as e:
            self.logger.error("Failed to send Ping: {}".format(e))

    def read_data(self):
        data = ""
        while True:
            try:
                op_code, frame = self.ws.recv_data_frame(True)
                try:
                    _message = json.loads(frame.data)
                    if "event" in _message:
                        if _message["event"] == "ping":
                            self._handle_heartbeat()
                except:
                    err_code = decode_ws_error_code(frame.data)
                    self.logger.warning(f"Websocket error code received: {err_code}")
            except WebSocketConnectionClosedException:
                self.logger.warning("WebSocket connection closed. Reconnecting...")
                self.reconnect()
                continue
            except WebSocketException as e:
                if isinstance(e, WebSocketTimeoutException):
                    self.logger.error("Websocket connection timeout")
                else:
                    self.logger.error(f"Websocket exception: {e}")
                self.reconnect()
                continue
            except Exception as e:
                self.logger.error(f"Exception in read_data: {e}")
                self.logger.warning("Reconnecting...")
                self.reconnect()
                continue
            self._handle_data(op_code, frame, data)

            if op_code == ABNF.OPCODE_CLOSE:
                self.logger.warning("CLOSE frame received, closing websocket connection")
                self._callback(self.on_close)
                break

    def _handle_data(self, op_code, frame, data):
        if op_code == ABNF.OPCODE_TEXT:
            data = frame.data.decode()
            self._callback(self.on_message, data)

    def close(self):
        if not self.ws.connected:
            self.logger.warning("Websocket already closed")
        else:
            self.ws.send_close()
        return

    def _callback(self, callback, *args):
        if callback:
            try:
                callback(self, *args)
            except Exception as e:
                self.logger.error("Error from callback {}: {}".format(callback, e))
                if self.on_error:
                    self.on_error(self, e)
