from tests.utils import mock_http_response, random_str
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()

create_order_params = {
    "symbol": "PERP_NEAR_USDC",
    "order_type": "LIMIT",
    "side": "BUY",
    "order_price": 1.3,
    "order_amount": 2
}

get_orders_params = {
    "symbol": "PERP_NEAR_USDC",
    "order_type": "LIMIT",
    "side": "BUY",
    "status": "FILLED"
}

get_trades_params = {
    "symbol": "PERP_NEAR_USDC"
}

delete_order_params = {
    "order_id": 15,
    "symbol": "PERP_NEAR_USDC",
}

delete_order_client_params = {
    "client_order_id": 15,
    "symbol": "PERP_NEAR_USDC",
}

batch_cancel_orders_params = "15,16,17"
batch_cancel_orders_client_params = "15,16,17"
order_id_param = "15"
trade_id_param = "15"


@mock_http_response(
    responses.POST,
    f"/v1/order",
    mock_data,
    200
)
def test_create_order():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.create_order(**create_order_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/batch-order",
    mock_data,
    200
)
def test_batch_create_order():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.batch_create_order([create_order_params, create_order_params])
    response.should.equal(mock_data)


@mock_http_response(
    responses.PUT,
    f"/v1/order",
    mock_data,
    200
)
def test_edit_order():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.edit_order(order_id="test_order_id", **create_order_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.DELETE,
    f"/v1/order\\?{urlencode(delete_order_params)}",
    mock_data,
    200
)
def test_cancel_order():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.cancel_order(**delete_order_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.DELETE,
    f"/v1/client/order\\?{urlencode(delete_order_client_params)}",
    mock_data,
    200
)
def test_cancel_order_client():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.cancel_order_by_client_order_id(**delete_order_client_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.DELETE,
    f"/v1/orders\\?symbol=PERP_NEAR_USDC",
    mock_data,
    200
)
def test_cancel_orders():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.cancel_orders(symbol='PERP_NEAR_USDC')
    response.should.equal(mock_data)


@mock_http_response(
    responses.DELETE,
    f"/v1/batch-order\\?order_ids={batch_cancel_orders_params}",
    mock_data,
    200
)
def test_batch_cancel_orders():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.batch_cancel_orders(batch_cancel_orders_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.DELETE,
    f"/v1/client/batch-order\\?client_order_ids={batch_cancel_orders_client_params}",
    mock_data,
    200
)
def test_batch_cancel_orders_client():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.batch_cancel_orders_by_client_order_id(batch_cancel_orders_client_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/order/{order_id_param}",
    mock_data,
    200
)
def test_get_order():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_order(order_id_param)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/client/order/{order_id_param}",
    mock_data,
    200
)
def test_get_order():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_order_by_client_order_id(order_id_param)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/orders\\?{urlencode(get_orders_params)}",
    mock_data,
    200
)
def test_get_orders():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_orders(**get_orders_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/orderbook/PERP_NEAR_USDC",
    mock_data,
    200
)
def test_get_orderbook_snapshot():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_orderbook_snapshot(symbol='PERP_NEAR_USDC')
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/order/{order_id_param}/trades",
    mock_data,
    200
)
def test_get_trades_of_order():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_all_trades_of_order(order_id_param)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/trades\\?{urlencode(get_trades_params)}",
    mock_data,
    200
)
def test_get_trades():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_trades(**get_trades_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/trade/{trade_id_param}",
    mock_data,
    200
)
def test_get_trade():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_trade(trade_id_param)
    response.should.equal(mock_data)
