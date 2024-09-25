import asyncio
from typing import Optional

import json
import logging
from orderly_evm_connector.lib.utils import (
    get_timestamp,
    orderlyLog,
    get_uuid,
    parse_proxies,
    generate_signature,
)
from orderly_evm_connector.websocket.orderly_socket_manager import OrderlySocketManager
from orderly_evm_connector.websocket.async_websocket_manager import AsyncWebsocketManager


class OrderlyWebsocketClient:
    def __init__(
        self,
        websocket_url,
        orderly_account_id=None,
        orderly_key=None,
        orderly_secret=None,
        private=False,
        wss_id=None,
        async_mode=False,
        timeout=None,
        debug=False,
        proxies: Optional[dict] = None,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
    ):
        orderly_account_id = (
            orderly_account_id
            if orderly_account_id
            else "OqdphuyCtYWxwzhxyLLjOWNdFP7sQt8RPWzmb5xY"
        )
        self.websocket_url = f"{websocket_url}/{orderly_account_id}"
        self.orderly_secret = orderly_secret
        self.wss_id = wss_id if wss_id else get_uuid()
        self.orderly_key = orderly_key
        self.private = private
        self.timeout = timeout
        self.logger = orderlyLog(debug=debug)
        self.subscriptions = []
        self._proxy_params = parse_proxies(proxies) if proxies else {}
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.on_error = on_error
        self.debug = debug
        if not async_mode:
            self._initialize_socket(
                self.websocket_url,
                self.wss_id,
                orderly_key,
                orderly_secret,
                on_message,
                on_open,
                on_close,
                on_error,
                timeout,
                debug,
                proxies,
            )
        self.logger.debug("Orderly WebSocket Client started.")


    async def run(self):
        manager = AsyncWebsocketManager(
            websocket_url=self.websocket_url,
            on_message=self.on_message,
            on_open=self.on_socket_open,
            on_close=self.on_close,
            on_error=self.on_error,
            debug=self.debug
        )
        asyncio.create_task(manager.run())
        await manager.ensure_init()

    def _auth_params(self):
        return {
            "id": self.wss_id,
            "event": "auth",
            "params": {
                "orderly_key": self.orderly_key,
                "sign": self._signature,
                "timestamp": self._timestamp,
            },
        }

    def _initialize_socket(
        self,
        websocket_url,
        wss_id,
        orderly_key,
        orderly_secret,
        on_message,
        on_open,
        on_close,
        on_error,
        timeout,
        debug,
        proxies,
    ):
        return OrderlySocketManager(
            websocket_url,
            on_message=on_message,
            on_open=self.on_socket_open,
            on_close=on_close,
            on_error=on_error,
            timeout=timeout,
            debug=debug,
            proxies=proxies,
        )

    def on_socket_open(self, socket_manager):
        self.logger.debug("Orderly WebSocket Connection opened. Subscribing...")
        if not hasattr(self, "socket_manager"):
            self.socket_manager = socket_manager
            self.socket_manager.start()
        if self.private:
            self.auth_login()
        for message in self.subscriptions:
            self.socket_manager.send_message(json.dumps(message))

    def auth_login(self):
        if not self.socket_manager._login:
            if self.orderly_secret:
                self._timestamp, self._signature = generate_signature(self.orderly_secret)
                self.auth_params = self._auth_params()
                self.auth_params['params']['timestamp'] = int(self.auth_params['params']['timestamp'])
            self.socket_manager.send_message(json.dumps(self.auth_params))
            self.socket_manager._login = True

    def send(self, message: dict):
        self.socket_manager.send_message(json.dumps(message))

    def send_message_to_server(self, message: dict):
        if self.private:
            self.auth_login()
        action = message["event"]
        if action and action != "unsubscribe":
            return self.subscribe(message)
        else:
            return self.unsubscribe(message)

    def subscribe(self, message):
        if str(message) not in self.subscriptions:
            self.subscriptions.append(message)
        self.socket_manager.send_message(json.dumps(message))

    def unsubscribe(self, message):
        self.socket_manager.send_message(json.dumps(message))

    def stop(self, id=None):
        self.socket_manager.close()
        self.socket_manager.join()
