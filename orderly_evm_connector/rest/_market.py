from orderly_evm_connector.lib.utils import check_required_parameters
from orderly_evm_connector.lib.utils import check_enum_parameter
from orderly_evm_connector.lib.enums import TimeType


def get_market_trades(self, symbol: str, limit: int = None):
    """Market trades
    Limit: 10 requests per 1 second per IP address

    GET /v1/public/market_trades

    Get the latest market trades.

    Args:
        symbol(string)
    Optional Args:
        limit(number): N (default: 10)	Numbers of trades want to query.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-market-trades
    """
    check_required_parameters([[symbol, "symbol"]])
    payload = {"symbol": symbol, "limit": limit}
    return self._request("GET", "/v1/public/market_trades", payload=payload)


def get_volume_statistics(self):
    """Volume statistics

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/volume/stats

    Get the latest volume statistics of Orderly and its associated brokers. Note that for broker volume, the volume is counted as the sum of the maker and taker volume, while for the full Orderly platform, the volume is the total amount matched on the platform (ie taker and maker are not double-counted.)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-volume-statistics
    """
    return self._request("GET", "/v1/public/volume/stats")


def get_predicted_funding_rate_for_all_markets(self):
    """Get predicted funding rate for all markets

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/funding_rates

    Get predicted funding rates for all futures trading pairs.

    Get the : * last_funding_rate : latest hourly funding rate for all the markets for the last funding period (dt = 8h) * est_funding_rate : rolling average of all funding rates over the last 8 hours

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-predicted-funding-rates-for-all-markets
    """
    return self._request("GET", "/v1/public/funding_rates")


def get_predicted_funding_rate_for_one_market(self, symbol: str):
    """Get predicted funding rate for one market

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/funding_rate/:symbol

    Get latest funding rate for one market.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-funding-rate-history-for-one-market
    """
    check_required_parameters([[symbol, "symbol"]])
    return self._request("GET", f"/v1/public/funding_rate/{symbol}")


def get_funding_rate_history_for_one_market(
    self,
    symbol: str,
    start_t: float = None,
    end_t: float = None,
    page: int = None,
    size: int = None,
):
    """Get funding rate history for one market

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/funding_rate_history

    Get funding rate history for one market.

    Args:
        symbol(string)
    Optional Args:
        start_t(timestamp): start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        end_t(timestamp): end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        page(number): N(default: 1)	the page you wish to query.
        size(number): Default: 60

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-funding-fee-history
    """
    check_required_parameters([[symbol, "symbol"]])
    payload = {
        "symbol": symbol,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
    }
    return self._request("GET", "/v1/public/funding_rate_history", payload=payload)


def get_futures_info_for_all_markets(self):
    """Get futures info for all markets

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/futures

    Get basic futures information for all the markets.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-futures-info-for-all-markets
    """
    return self._request("GET", "/v1/public/futures")


def get_futures_info_for_one_market(self, symbol: str):
    """Get futures for one market

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/futures/:symbol

    Get basic futures information for one market.

    Args:
        symbol(string)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-futures-info-for-one-market
    """
    check_required_parameters([[symbol, "symbol"]])
    _uri = f"/v1/public/futures/{symbol}"
    return self._request("GET", _uri)


def get_tradingview_configuration(self, locale: str):
    """Get TradingView localized configuration info

    Limit: 10 requests per 1 second per IP address

    GET /v1/tv/config

    Args:
        locale(string)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-tradingview-localized-config-info
    """
    check_required_parameters([[locale, "locale"]])
    payload = {"locale": locale}
    self._request("GET", "/v1/tv/config", payload=payload)


def get_tradingview_history_basrs(
    self, symbol: str, resolution: str, from_timestamp=0, to_timestamp=0
):
    """Get TradingView history bars

    Limit: 10 requests per 1 second per IP address

    GET /v1/tv/history

    Args:
        symbol(string)
        resolution(string)
        from(timestamp)
        to(timestamp)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-tradingview-history-bars

    """

    check_required_parameters(
        [
            [symbol, "symbol"],
            [resolution, "resolution"],
            [from_timestamp, "from_timestamp"],
            [to_timestamp, "to_timestamp"],
        ]
    )
    payload = {
        "symbol": symbol,
        "resolution": resolution,
        "from": from_timestamp,
        "to": to_timestamp,
    }
    self._request("GET", "/v1/tv/history", payload=payload)


def get_tradingview_symbol_info(self, group: str):
    """Get TradingView symbol info

    Limit: 10 requests per 1 second per IP address

    GET /v1/tv/symbol_info

    Args:
        group(string)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-tradingview-symbol-info
    """
    check_required_parameters([[group, "group"]])
    payload = {"group": group}
    self._request("GET", "/v1/tv/symbol_info", payload=payload)


def get_orderbook_snapshot(self, symbol: str, max_level: int = None):
    """[Private] Orderbook snapshot

    Limit: 10 requests per 1 second

    GET /v1/orderbook/:symbol

    Snapshot of the current orderbook. Price of asks/bids are in descending order.

    Optional Args:
        max_level(number): (default: 100)	the levels wish to show on both side.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/orderbook-snapshot
    """

    check_required_parameters([[symbol, "symbol"]])
    payload = {"max_level": max_level}
    return self._sign_request("GET", f"/v1/orderbook/{symbol}", payload=payload)


def get_kline(self, symbol: str, type: str, limit: int = None):
    """Get kline
    Limit: 10 requests per 1 second

    GET /v1/kline

    Get the latest klines (OHLC) of the trading pairs.

    Args:
        symbol(string)
        type(enum): 1m/5m/15m/30m/1h/4h/12h/1d/1w/1mon/1y

    Optional Args:
        limit(number): Numbers of klines. Maximum of 1000 klines.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-kline
    """
    check_required_parameters([[symbol, "symbol"], [type, "type"]])
    check_enum_parameter(f"_{type}", TimeType)
    payload = {"symbol": symbol, "type": type, "limit": limit}
    return self._sign_request("GET", "/v1/kline", payload=payload)
