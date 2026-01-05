def request_orderbook(self, type: str, symbol: str):
    """
    Request orderbook data
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/request-orderbook
    """

    _message = {
        "id": self.wss_id,
        "event": "request",
        "params": {"type": type, "symbol": symbol},
    }
    self.send(_message)


def get_orderbook(self, topic: str):
    """
    {symbol}@orderbook depth 100 push every 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/orderbook
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_orderbookupdate(self, topic: str):
    """
    {symbol}@orderbookupdate updated orderbook push every 200ms
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/order-book-update
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_trade(self, topic: str):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/trade
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_24h_ticker(self, topic: str):
    """
    Push interval: 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/24-hour-ticker
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_24h_tickers(self):
    """
    Push interval: 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/24-hour-tickers
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": "tickers"}
    self.send_message_to_server(_message)


def get_24h_ticker_by_builder(self, broker_id: str, symbol: str):
    """
    Push interval: 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/24-hour-ticker-by-builder
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": broker_id + "$" + symbol + "@ticker"}
    self.send_message_to_server(_message)


def get_24h_tickers_by_builder(self, broker_id: str):
    """
    Push interval: 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/24-hour-tickers-by-builder
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": broker_id + "$tickers"}
    self.send_message_to_server(_message)


def get_bbo(self, topic: str):
    """
    Push interval: 10ms
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/bbo
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": topic}
    self.send_message_to_server(_message)


def get_bbos(self):
    """
    Push interval: 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/bbos
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": "bbos",
    }
    self.send_message_to_server(_message)


def get_kline(self, topic: str):
    """
    {time}: 1m/5m/15m/30m/1h/1d/1w/1M
    Push interval: 1s
    Name	Type	Required	Description
    id	    string	Y	        id generate by client
    event	string	Y	        subscribe/unsubscribe
    topic	string	N	        {symbol}@kline_{time}
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/k-line
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_market_price_changes_info(self):
    """
    Push interval: every 1m
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/price-changes
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": "price_changes",
    }
    self.send_message_to_server(_message)


def get_traders_open_interest(self):
    """
    Push interval: every 1m
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/traders-open-interests
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": "traders_open_interests",
    }
    self.send_message_to_server(_message)


def get_price_for_small_charts(self, time_interval: str):
    """
    Push interval: every 1m
    * 1h (1 hour)
    * 4h (4 hours)
    * 12h (12 hours)
    * 1d (1 day)
    * 1w (1 week)
    * 1M (1 month)
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/price-for-small-charts
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": "history_charts_" + time_interval,
    }
    self.send_message_to_server(_message)


def get_index_price(self, topic: str):
    """
    Push interval: 1s
    For index price, use SPOT symbol such as SPOT_ETH_USDC instead of PERP_ETH_USDC
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/index-price
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_index_prices(self):
    """
    Push interval: 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/index-prices
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": "indexprices",
    }
    self.send_message_to_server(_message)


def get_mark_price(self, topic: str):
    """
    Push interval: 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/mark-price
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_mark_prices(self):
    """
    Push interval: 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/mark-prices
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": "markprices",
    }
    self.send_message_to_server(_message)


def get_open_interest(self, topic: str):
    """
    Push interval: push every 1 second if open interest change and 10 seconds force update even if no change
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/open-interest
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_estimated_funding_rate(self, topic: str):
    """
    Push interval: 15s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/estimated-funding-rate
    """
    _message = {
        "id": self.wss_id,
        "event": "subscribe",
        "topic": topic,
    }
    self.send_message_to_server(_message)


def get_liquidation_push(self):
    """
    Push interval: push on addition/removal/update from list within 1s
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/liquidation-push
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": "liquidation"}
    self.send_message_to_server(_message)


def get_system_maintenance_status(self):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/system-maintenance-status
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": "maintenance_status"}
    self.send_message_to_server(_message)


def get_announcement(self):
    """
    Push interval: on new announcement
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/public/announcement
    """
    _message = {"id": self.wss_id, "event": "subscribe", "topic": "announcement"}
    self.send_message_to_server(_message)
