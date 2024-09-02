from orderly_evm_connector.lib.utils import check_required_parameters
from orderly_evm_connector.lib.utils import check_enum_parameter
from orderly_evm_connector.lib.enums import OrderType, OrderStatus, OrderSide,AlgoType

def create_order(
    self,
    symbol: str,
    order_type: str,
    side: str,
    client_order_id: str = None,
    order_price: float = None,
    order_quantity: float = None,
    order_amount: float = None,
    reduce_only: bool = None,
    visible_quantity: float = None,
):
    """[Private] Create order

    Limit: 10 requests per 1 second

    POST /v1/order

    Args:
        symbol（string)
        order_type(enum): LIMIT/MARKET/IOC/FOK/POST_ONLY/ASK/BID
        side(enum): SELL/BUY
    Optional Args:
        client_order_id(string): 36 length, default: null
        order_price(number): If order_type is MARKET/ASK/BID, then is not required, otherwise this parameter is required.
        order_quantity(number): For MARKET/ASK/BID order, if order_amount is given, it is not required.
        order_amount(number): For MARKET/ASK/BID order, the order size in terms of quote currency
        reduce_only(boolean): Default False
        visible_quantity(number): The order quantity shown on orderbook. (default: equal to order_quantity)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/create-order
    """
    check_required_parameters(
        [[symbol, "symbol"], [order_type, "order_type"], [side, "side"]]
    )
    check_enum_parameter(order_type, OrderType)
    payload = {
        "symbol": symbol,
        "order_type": order_type,
        "side": side,
        "client_order_id": client_order_id,
        "order_price": order_price,
        "order_quantity": order_quantity,
        "order_amount": order_amount,
        "reduce_only": reduce_only,
        "visible_quantity": visible_quantity,
    }
    return self._sign_request("POST", "/v1/order", payload=payload)

def create_algo_order(
    self,
    algo_type: str,
    quantity: int,
    side: str,
    symbol: str,
    type: str,
    trigger_price: float,
    child_orders: list = [],
    client_order_id: str = None,
    order_tag: str = None,
    price: float = None,
    reduce_only: bool = None,
    visible_quantity: bool = None,
    trigger_price_type: str = "MARK_PRICE",
):
    """[Private] Place maker/taker order that requires an additional trigger for order execution such as stop orders.

STOP type order bahavior: an order to buy or sell at the market price once the asset has traded at or through a specified price (the “stop price”). If the asset reaches the stop price, the order becomes a market order and is filled at the next available market price.

Note: This endpoint requires trading scope in Orderly Key.

    Limit: 10 requests per 1 second

    POST /v1/algo/order

    Args:
        algo_type(string)：Only STOP is available for now
        quantity(number): For MARKET/ASK/BID order, if order_amount is given, it is not required.
        side(string): SELL/BUY
        symbol(string)
        type(string):LIMIT/MARKET
        trigger_price_type(number): Only MARK_PRICE is available for now.
        trigger_price(number)

    Optional Args:
        client_order_id(string): 36 length, default: null
        order_tag(string)
        price(number)
        reduce_only(boolean): Default False
        visible_quantity(boolean): Default false

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/create-algo-order
    """
    check_required_parameters(
        [[algo_type, "algo_type"], [quantity, "quantity"], [side, "side"], [symbol, "symbol"], [type, "type"], [trigger_price, "trigger_price"]]
    )
    payload = {
        "algo_type": algo_type,
        "client_order_id": client_order_id,
        "order_tag": order_tag,
        "price": price,
        "quantity": quantity,
        "reduce_only": reduce_only,
        "side": side,
        "symbol": symbol,
        "trigger_price": trigger_price,
        "trigger_price_type": trigger_price_type,
        "type": type,
        "child_orders": child_orders,
        "visible_quantity": visible_quantity
    }
    return self._sign_request("POST", "/v1/algo/order", payload=payload)

def batch_create_order(self, orders: list):
    """[Private] Batch create order
    Limit: 1 request per 1 second

    POST /v1/batch-order

    Creates a batch of orders as a list according to the same rules as a single Create Order.

    Parameters for each order within the batch will be the same as the create single order. The batch of orders should be sent as a JSON array containing all the orders. The maximum number of orders that can be sent in 1 batch order request is 10. Each order within the batch order request is counted as 1 order towards the overall create order rate limit.

    Args:
        symbol(string)
        order_type(enum): LIMIT/MARKET/IOC/FOK/POST_ONLY/ASK/BID
        side(enum): SELL/BUY
    Optional Args:
        client_order_id(string):	36 length, default: null
        order_price	number	N	If order_type is MARKET, then is not required, otherwise this parameter is required.
        order_quantity	number	N	For MARKET/ASK/BID order, if order_amount is given, it is not required.
        order_amount	number	N	For MARKET/ASK/BID order, the order size in terms of quote currency
        reduce_only	boolean	N	Default False
        visible_quantity	number	N	The order quantity shown on orderbook. (default: equal to order_quantity)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/batch-create-order
    """
    for order in orders:
        check_required_parameters(
            [
                [order["symbol"], "symbol"],
                [order["order_type"], "order_type"],
                [order["side"], "side"],
            ]
        )
        check_enum_parameter(order["order_type"], OrderType)

    payload = {"orders": orders}
    return self._sign_request("POST", "/v1/batch-order", payload=payload)

def edit_algo_order(
    self,
    order_id: str,
    price: float = None,
    quantity: int = None,
    trigger_price: float = None

):
    """[Private] Edit a pending algo order by order_id. Only the price or quantity can be amended.
    Limit: 10 request per 1 second

    PUT /v1/algo/order

    Edit a pending algo order by order_id. Only the price or quantity can be amended.

    Note: This endpoint requires trading scope in Orderly Key.
    Args:
        order_id(string)        
    Optional Args:
        price(number)
        quantity(number)
        trigger_price(number)
    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/edit-algo-order
    """
    check_required_parameters(
        [
            [order_id, "order_id"],
        ]
    )

    payload = {
        "order_id": order_id,
        "price": price,
        "quantity": quantity,
        "trigger_price": trigger_price
    }
    return self._sign_request("PUT", "/v1/algo/order", payload=payload)

def edit_order(
    self,
    order_id: str,
    symbol: str,
    order_type: str,
    side: str,
    client_order_id: str = None,
    order_price: float = None,
    order_quantity: float = None,
    order_amount: float = None,
    reduce_only: bool = None,
    visible_quantity: float = None,
):
    """[Private] Edit order
    Limit: 10 request per 1 second

    PUT /v1/order

    Edit a pending order by order_id. Only the order_price or order_quantity can be amended.

    Args:
        order_id(string)
        symbol(string)
        order_type(enum): LIMIT/MARKET/IOC/FOK/POST_ONLY/ASK/BID
        side(enum): SELL/BUY
    Optional Args:
        client_order_id(string):	36 length, default: null
        order_price	number	N	If order_type is MARKET, then is not required, otherwise this parameter is required.
        order_quantity	number	N	For MARKET/ASK/BID order, if order_amount is given, it is not required.
        order_amount	number	N	For MARKET/ASK/BID order, the order size in terms of quote currency
        reduce_only	boolean	N	Default False
        visible_quantity	number	N	The order quantity shown on orderbook. (default: equal to order_quantity)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/edit-order

    """
    check_required_parameters(
        [
            [order_id, "order_id"],
            [symbol, "symbol"],
            [order_type, "order_type"],
            [side, "side"],
        ]
    )
    check_enum_parameter(order_type, OrderType)

    payload = {
        "order_id": order_id,
        "order_price": order_price,
        "order_quantity": order_quantity,
        "order_type": order_type,
        "side": side,
        "symbol": symbol,
        "client_order_id": client_order_id,
        "order_amount": order_amount,
        "reduce_only": reduce_only,
        "visible_quantity": visible_quantity,
    }
    return self._sign_request("PUT", "/v1/order", payload=payload)

def cancel_algo_order(self, order_id: int, symbol: str):
    """[Private] Cancel Algo Order

    Limit: 10 requests per 1 second

    DELETE /v1/algo/order?order_id={order_id}&symbol={symbol}

    Cancel a single algo order by order_id.

    Args:
        order_id(number)
        symbol(string)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/cancel-algo-order
    """
    self.session.headers.update(
            {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )
    check_required_parameters([[order_id, "order_id"], [symbol, "symbol"]])
    return self._sign_request("DELETE", f"/v1/algo/order?order_id={order_id}&symbol={symbol}")

def cancel_algo_all_pending_order(self, symbol: str, algo_type: str):
    """[Private] Cancel All Pending Algo Orders

    Limit: 10 requests per 1 second

    DELETE /v1/algo/orders?symbol={symbol}

    Cancel all pending algo orders.

    Args:
        symbol(string)
        algo_type(string): STOP, TAKE_PROFIT, STOP_LOSS, TP_SL, POSITIONAL_TP_SL, BRACKET

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/cancel-all-pending-algo-orders
    """
    self.session.headers.update(
            {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )
    check_enum_parameter(algo_type, AlgoType)
    check_required_parameters([[symbol, "symbol"]])
    # add symbol and algo type if they are not None
    url = f"/v1/algo/orders"
    if symbol and algo_type:
        url += f"?symbol={symbol}&algo_type={algo_type}"
    elif symbol:
        url += f"?symbol={symbol}"
    elif algo_type:
        url += f"?algo_type={algo_type}"

    return self._sign_request("DELETE", url)

def cancel_order(self, order_id: int, symbol: str, **kwargs):
    """[Private] Cancel order

    Limit: 10 requests per 1 second

    DELETE /v1/order?order_id=:oid&symbol=:symbol

    Cancels a single order by order_id.

    Args:
        symbol(string)
        order_id(number)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/cancel-order
    """
    check_required_parameters([[order_id, "order_id"], [symbol, "symbol"]])
    payload = {"order_id": order_id, "symbol": symbol}
    return self._sign_request("DELETE", "/v1/order", payload=payload)

def cancel_algo_order_by_client_order_id(self, client_order_id: int, symbol: str):
    """[Private] Cancel Algo Order By client_order_id

    Limit: 10 requests per 1 second

    DELETE /v1/algo/client/order?client_order_id={client_order_id}&symbol={symbol}

    Cancel an algo order by client_order_id.

    Args:
        symbol(string)
        client_order_id(string): client_order_id of the algo order

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/cancel-algo-order-by-client_order_id    """
    check_required_parameters(
        [[client_order_id, "client_order_id"], [symbol, "symbol"]]
    )
    self.session.headers.update(
            {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )
    return self._sign_request("DELETE", f"/v1/algo/client/order?client_order_id={client_order_id}&symbol={symbol}")


def cancel_order_by_client_order_id(self, client_order_id: int, symbol: str):
    """[Private] Cancel order by client_order_id

    Limit: 10 requests per 1 second

    DELETE /v1/client/order?client_order_id=:coid&symbol=:symbol

    Cancel an order by client_order_id.

    Args:
        symbol(string)
        client_order_id(string): client_order_id of the order

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/cancel-order-by-client_order_id
    """
    check_required_parameters(
        [[client_order_id, "client_order_id"], [symbol, "symbol"]]
    )
    payload = {"client_order_id": client_order_id, "symbol": symbol}
    return self._sign_request("DELETE", "/v1/client/order", payload=payload)


def cancel_orders(self, symbol: str = None):
    """[Private] Cancel orders in bulk

    Limit: 10 requests per 1 second

    DELETE /v1/orders?symbol=:symbol

    Cancel a list of orders, filtered by symbol optionally. This request will cancel all open orders within the filter criteria, and will cancel all open orders if no filter is provided.

    Optional Args:
        symbol(string)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/cancel-orders-in-bulk
    """
    payload = {"symbol": symbol}
    return self._sign_request("DELETE", "/v1/orders", payload=payload)


def batch_cancel_orders(self, order_ids: str):
    """[Private] Batch cancel orders

    Limit: 10 requests per 1 second

    DELETE /v1/batch-order?order_ids=:order_id_1,:order_id_2

    Cancel a list of orders by order_id. The maximum orders that can be cancelled within 1 batch cancel request is 10.

    Args:
        order_ids(string): list of order_ids, comma-separated, with a maximum of 10 order ids per request.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/batch-cancel-orders
    """
    check_required_parameters([[order_ids, "order_ids"]])
    payload = {"order_ids": order_ids}
    return self._sign_request("DELETE", "/v1/batch-order", payload=payload)


def batch_cancel_orders_by_client_order_id(self, client_order_ids: str):
    """[Private] Batch cancel orders by client_order_id

    Limit: 10 requests per 1 second

    DELETE /v1/client/batch-order?client_order_ids=:order_id_1,:order_id_2

    Cancel a list of orders by client_order_id. The maximum orders that can be cancelled within 1 batch cancel request is 10.

    Args:
        client_order_ids(string): list of order_ids, comma-separated, with a maximum of 10 order ids per request.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/batch-cancel-orders-by-client_order_id
    """
    check_required_parameters([[client_order_ids, "client_order_ids"]])
    # payload = {"client_order_ids": ",".join(client_order_ids)}
    payload = {"client_order_ids": client_order_ids}
    return self._sign_request("DELETE", "/v1/client/batch-order", payload=payload)

def get_algo_order(self, order_id: str):
    """[Private] Get order

    Limit: 10 requests per 1 second

    GET /v1/algo/order/{order_id}

    Get details of a single algo order by order_id.

    Args:
        order_id(string): id of the algo order

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-algo-order
    """
    check_required_parameters([[order_id, "order_id"]])
    return self._sign_request("GET", f"/v1/algo/order/{order_id}")

def get_order(self, order_id: str):
    """[Private] Get order

    Limit: 10 requests per 1 second

    GET /v1/order/:order_id

    Get details of a single order by order_id.

    Args:
        order_id(number): id of the order

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-order
    """
    check_required_parameters([[order_id, "order_id"]])
    return self._sign_request("GET", f"/v1/order/{ order_id }")

def get_algo_order_by_client_order_id(self, client_order_id: str):
    """[Private] Get Algo Order by client_order_id

    Limit: 10 requests per 1 second

    GET /v1/algo/client/order/{client_order_id}

    Get details of a single algo order by client_order_id.

    Args:
        client_order_id(string): client id of the order

    """
    check_required_parameters([[client_order_id, "client_order_id"]])
    return self._sign_request("GET", f"/v1/algo/client/order/{client_order_id}")


def get_order_by_client_order_id(self, client_order_id: str):
    """[Private] Get order by client_order_id

    Limit: 10 requests per 1 second

    GET /v1/client/order/:client_order_id

    Get details of a single order by client_order_id.

    Args:
        client_order_id(string): client id of the order

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-order-by-client_order_id
    """
    check_required_parameters([[client_order_id, "client_order_id"]])
    return self._sign_request("GET", f"/v1/client/order/{ client_order_id }")

def get_algo_orders(
    self,
    algo_type: str,
    symbol: str = None,
    order_type: str = None,
    status: str = None,
    start_t: float = None,
    end_t: float = None,
    side: str = None,
    page: int = None,
    size: int = None,
    is_triggered: str = None,
    order_tag: str = None
    
):
    """[Private] Get Algo Orders

    Limit: 10 requests per 1 second

    GET /v1/algo/orders

    Get algo order details by customized filters.

    For filter by status, one can reference special bundled statuses below for ease of access of Open (i.e INCOMPLETE) orders or COMPLETED orders.

    INCOMPLETE = NEW + PARTIAL_FILLED

    COMPLETED = CANCELLED + FILLED

    Optional Args:
    symbol(string)
    side(string):	BUY/SELL
    order_type(string):	LIMIT/MARKET
    status(enum): NEW/CANCELLED/PARTIAL_FILLED/FILLED/REJECTED/INCOMPLETE/COMPLETED
    start_t(timestamp): start time range that wish to query, noted the time stamp is 13-digits timestamp.
    end_t(timestamp): end time range that wish to query, noted the time stamp is 13-digits timestamp.
    page(number): (default: 1)	the page you wish to query.
    size(number): (default: 25)	the page size you wish to query (max: 500)
    algo_type(string)
    is_triggered(string)
    order_tag(string)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-algo-orders#openapi-evmopenapi-get-v1algoorders
    """
    if order_type:
        check_enum_parameter(order_type, OrderType)
    if side:
        check_enum_parameter(side, OrderSide)
    if status:
        check_enum_parameter(status, OrderStatus)

    check_required_parameters([[algo_type, "algo_type"]])

    payload = {
        "symbol": symbol,
        "order_type": order_type,
        "side": side,
        "status": status,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
        "algo_type": algo_type,
        "is_triggered": is_triggered,
        "order_tag": order_tag
    }
    return self._sign_request("GET", "/v1/algo/orders", payload=payload)

def get_orders(
    self,
    symbol: str = None,
    order_type: str = None,
    side: str = None,
    status: str = None,
    start_t: float = None,
    end_t: float = None,
    page: int = None,
    size: int = None,
    order_tag: str = None,
    source_type: str = None,
    sort_by: str = None
):
    """[Private] Get orders

    Limit: 10 requests per 1 second

    GET /v1/orders

    Get orders by customized filters.

    For filter by status, one can reference special bundled statuses below for ease of access of Open (ie INCOMPLETE) orders or COMPLETED orders.

    INCOMPLETE = NEW + PARTIAL_FILLED
    COMPLETED = CANCELLED + FILLED

    Optional Args:
    symbol(string)
    side(string):	BUY/SELL
    order_type(string):	LIMIT/MARKET
    status(enum): NEW/CANCELLED/PARTIAL_FILLED/FILLED/REJECTED/INCOMPLETE/COMPLETED
    start_t(timestamp): start time range that wish to query, noted the time stamp is 13-digits timestamp.
    end_t(timestamp): end time range that wish to query, noted the time stamp is 13-digits timestamp.
    page(number): (default: 1)	the page you wish to query.
    size(number): (default: 25)	the page size you wish to query (max: 500)
    order_tag(string)
    sort_by(string)
    If empty:

    Descending order by updated_time if user passed update_start_t or update_end_t; descending order by order_id if updated_time are the same;

    Otherwise descending order by created_time; descending order by order_id if created_time are the same;

    If not empty:

    If sort_by == CREATED_TIME_DESC, descending order by created_time. Descending order by order_id if created_time are same;

    If sort_by == CREATED_TIME_ASC, ascending order by created_time. Ascending order by order_id if created_time are same;

    If sort_by == UPDATED_TIME_DESC, descending order by updated_time. Descending order by order_id if updated_time are same;

    If sort_by == UPDATED_TIME_ASC, ascending order by updated_time. Ascending order by order_id if updated_time are same;
    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-orders#openapi-evmopenapi-get-v1orders
    """
    if order_type:
        check_enum_parameter(order_type, OrderType)
    if side:
        check_enum_parameter(side, OrderSide)
    if status:
        check_enum_parameter(status, OrderStatus)

    payload = {
        "symbol": symbol,
        "order_type": order_type,
        "side": side,
        "status": status,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
        "order_tag": order_tag,
        "sort_by":sort_by,
        "source_type": source_type
    }
    return self._sign_request("GET", "/v1/orders", payload=payload)


def get_all_trades_of_order(self, order_id: int):
    """[Private] Get all trades of a specific order

    Limit: 10 requests per 1 second

    GET /v1/order/:order_id/trades

    Get specific trades of an order by order_id.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-all-trades-of-specific-order

    """
    check_required_parameters([[order_id, "order_id"]])
    return self._sign_request("GET", f"/v1/order/{order_id}/trades")


def get_trades(
    self,
    symbol: str = None,
    start_t: float = None,
    end_t: float = None,
    page: int = None,
    size: int = None,
):
    """[Private] Get trades

    Limit: 10 requests per 1 second

    GET /v1/trades

    Return client’s trades history within a time range.

    Optional Args:
    symbol(string)
    start_t(timestamp): start time range that wish to query, noted the time stamp is 13-digits timestamp.
    end_t(timestamp): end time range that wish to query, noted the time stamp is 13-digits timestamp.
    page(number): (default: 1)	the page you wish to query.
    size(number): (default: 25)	the page size you wish to query. (max: 500)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-trades
    """
    payload = {
        "symbol": symbol,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
    }
    return self._sign_request("GET", "/v1/trades", payload=payload)


def get_trade(self, trade_id: int):
    """[Private] Get trade
    Limit: 10 requests per 1 second

    GET /v1/trade/:trade_id

    Get specific transaction details by trade_id.

    Args:
        trade_id(number): id of the trade

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-trade
    """
    check_required_parameters([[trade_id, "trade_id"]])
    return self._sign_request("GET", f"/v1/trade/{trade_id}")


def get_all_positions_info(self):
    """Get all position info

    Limit: 30 requests per 10 second per user

    GET /v1/positions

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-all-positions-info
    """
    _uri = "/v1/positions"
    return self._sign_request("GET", _uri)


def get_one_position_info(self, symbol: str):
    """Get one position info

    Limit: 30 requests per 10 second per user

    GET /v1/position/:symbol

    Args:
        symbol(string)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-one-position-info
    """
    check_required_parameters([[symbol, "symbol"]])
    _uri = f"/v1/position/{symbol}"
    return self._sign_request("GET", _uri)


def get_funding_fee_history(self, symbol: str, **kwargs):
    """Get funding fee history

    Limit: 20 requests per 60 second per user

    GET /v1/funding_fee/history

    Get funding fee history.

    Args:
        symbol(str)

    Optional Args:
        start_t(timestamp):	 start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        end_t(timestamp): end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.
        page(number): N(default: 1)	the page you wish to query.
        size(number): Default: 60
    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-funding-fee-history

    """
    check_required_parameters([[symbol, "symbol"]])
    payload = {"symbol": symbol, **kwargs}
    return self._sign_request("GET", "/v1/funding_fee/history", payload=payload)
