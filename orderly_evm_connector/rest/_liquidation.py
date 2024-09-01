from orderly_evm_connector.lib.utils import check_required_parameters, get_timestamp


def get_positions_under_liquidation(self, **kwargs):
    """Get positions under liquidation

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/liquidation

    Optional Args:
        start_t(timestamp): start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        end_t(timestamp): end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        page(number):  (default: 1)	the page you wish to query.
        size(number):  Default: 60

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-positions-under-liquidation
    """
    payload = {**kwargs}
    return self._request("GET", "/v1/public/liquidation", payload=payload)


def get_liquidated_positions_info(self, symbol: str = None, start_t: int = None, end_t: int = None, page: int = None, size: int = None):
    """Get liquidated positions info

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/liquidated_positions

    Args:
        symbol(string)
    Optional Args:
        tart_t(timestamp): start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        end_t(timestamp): end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        page(number):  (default: 1)	the page you wish to query.
        size(number):  Default: 60


    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-liquidated-positions-info
    """
    payload = {}
    if start_t:
        payload["start_t"] = start_t
    if end_t:
        payload["end_t"] = end_t
    if page:
        payload["page"] = page
    if size:
        payload["size"] = size
    if symbol:
        payload["symbol"] = symbol
    return self._request("GET", "/v1/public/liquidated_positions", payload=payload)


def get_insurance_fund_info(self):
    """Get insurance fund info

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/insurancefund

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-insurance-fund-info

    """
    return self._request("GET", "/v1/public/insurancefund")


def get_liquidated_positions_by_liquidator(self, symbol: str, **kwargs):
    """Get liquidated positions by Liquidator

    Limit: 10 requests per 1 second per IP address

    GET /v1/client/liquidator_liquidations

    Args:
        symbol(string)
    Optional Args:
        start_t(timestamp): start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        end_t(timestamp): end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        page(number):  (default: 1)	the page you wish to query.
        size(number):  Default: 60

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-liquidated-positions-by-liquidator
    """
    check_required_parameters([[symbol, "symbol"]])
    payload = {"symbol": symbol, **kwargs}
    return self._sign_request(
        "GET", "/v1/client/liquidator_liquidations", payload=payload
    )


def get_liquidated_positions_of_account(self, **kwargs):
    """Get liquidated positions of account

    Limit: 10 requests per 1 second per IP address

    GET /v1/liquidations

    Optional Args:
        symbol(string)
        start_t(timestamp)
        end_t(timestamp)
        page(number)
        size(number)
    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-liquidated-positions-of-account
    """
    payload = {**kwargs}
    return self._sign_request("GET", "/v1/liquidations", payload=payload)


def claim_liquidated_positions(self, liquidation_id: int, ratio_qty_request, **kwargs):
    """Claim liquidated positions

    Limit: 5 requests per 1 second per IP address

    POST /v1/liquidation

    Args:
        liquidation_id(number)
        ratio_qty_request(number)
    Optional Args:
        extra_liquidation_ratio(number)
        limit_price(json): Liquidator’s instruction to let the system reject the liquidation claim if the following condition applies: if position_qty > 0, reject if mark_price > limit_price; if position_qty < 0, reject if mark_price < limit_price
        limit_price.{symbol}(number): The limit price for each symbol in the liquidation claim
        symbols: For high risk tiers only
            symbols.ratio_qty_request(number, required): Field dedicated to high risk symbols liquidations type only (symbols with liquidation tier = 2), where a liquidator can specific the ratio he wish to liquidates per symbol
            symbols.symbol(string, required): Only relevant if this is a liquidation of type high tier (symbols with liquidation tier = 2)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/claim-liquidated-positions
    """
    check_required_parameters(
        [[liquidation_id, "liquidation_id"], [ratio_qty_request, "ratio_qty_request"]]
    )
    payload = {
        "liquidation_id": liquidation_id,
        "ratio_qty_request": ratio_qty_request,
        **kwargs,
    }
    return self._sign_request("POST", "/v1/liquidation", payload=payload)

def claim_from_insurance_fund(
    self, liquidation_id: str, symbol: str, qty_request, **kwargs
):
    """Claim from insurance fund

    Limit: 5 requests per 1 second

    POST /v1/claim_insurance_fund
    Args:
        liquidation_id(number)
        symbol(string)
        qty_request(number): Quantity to be claimed from insurance fund
    Optional Args:
        limit_price(number)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/claim-insurance-fund
    """
    check_required_parameters(
        [
            [liquidation_id, "liquidation_id"],
            [symbol, "symbol"],
            [qty_request, "qty_request"],
        ]
    )
    payload = {
        "liquidation_id": liquidation_id,
        "symbol": symbol,
        "qty_request": qty_request,
        **kwargs,
    }
    return self._sign_request("POST", "/v1/claim_insurance_fund", payload=payload)