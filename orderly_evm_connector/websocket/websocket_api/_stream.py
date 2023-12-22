from orderly_evm_connector.lib.utils import check_required_parameters


def request_orderbook(self, type: str, symbol: str):
    """Request orderbook data
    https://docs-api-evm.orderly.network/?shell#websocket-api-public-request-orderbook
    """

    _message = {
        "id": self.wss_id,
        "event": "request",
        "params": {"type": type, "symbol": symbol},
    }
    self.send(_message)


def get_orderbook(self, topic: str):
    """{symbol}@orderbook depth 100 push every 1s

    https://docs-api-evm.orderly.network/?shell#websocket-api-public-orderbook
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_orderbookupdate(self, topic: str):
    """{symbol}@orderbookupdate updated orderbook push every 200ms

    https://docs-api-evm.orderly.network/#websocket-api-public-order-book-update
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_trade(self, topic: str):
    """Push interval: real-time push

    https://docs-api-evm.orderly.network/#websocket-api-public-trade
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_24h_ticker(self, topic: str):
    """Push interval: 1s

    https://docs-api-evm.orderly.network/#websocket-api-public-24h-ticker
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_24h_tickers(self):
    """Push interval: 1s

    https://docs-api-evm.orderly.network/#websocket-api-public-24h-tickers
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": "tickers"}
    self.send_message_to_server(_message)


def get_bbo(self, topic: str):
    """Push interval: 10ms

    https://docs-api-evm.orderly.network/#websocket-api-public-bbo
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_bbos(self):
    """Push interval: 1s
    https://docs-api-evm.orderly.network/#websocket-api-public-bbos
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": "bbos",
    }
    self.send_message_to_server(_message)


def get_kline(self, topic: str):
    """{time}: 1m/5m/15m/30m/1h/1d/1w/1M
    Push interval: 1s
    Name	Type	Required	Description
    id	    string	Y	        id generate by client
    event	string	Y	        subscribe/unsubscribe
    topic	string	N	        {symbol}@kline_{time}

    https://docs-api-evm.orderly.network/#websocket-api-public-k-line
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_index_price(self, topic: str):
    """Push interval: 1s
    https://docs-api-evm.orderly.network/#websocket-api-public-index-price
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_index_prices(self):
    """Push interval: 1s
    https://docs-api-evm.orderly.network/#websocket-api-public-index-prices
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": "indexprices",
    }
    self.send_message_to_server(_message)


def get_mark_price(self, topic: str):
    """Push interval: 1s
    https://docs-api-evm.orderly.network/#websocket-api-public-mark-price
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_mark_prices(self):
    """Push interval: 1s
    https://docs-api-evm.orderly.network/#websocket-api-public-mark-prices
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": "markprices",
    }
    self.send_message_to_server(_message)


def get_open_interest(self, topic: str):
    """Push interval: push every 1 second if open interest change and 10 seconds force update even if no change.
    https://docs-api-evm.orderly.network/#websocket-api-public-open-interest
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_estimated_funding_rate(self, topic: str):
    """Push interval: 15s.
    https://docs-api-evm.orderly.network/#websocket-api-public-estimated-funding-rate
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_liquidation_push(self):
    """Push interval: push on addition/removal/update from list within 1s.
    https://docs-api-evm.orderly.network/#websocket-api-public-liquidation-push
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": "liquidation"}
    self.send_message_to_server(_message)
