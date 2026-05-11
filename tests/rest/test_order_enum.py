from tests.utils import mock_http_response, random_str
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses


mock_data = {"key_1": "value_1", "key_2": "value_2"}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()

broker_order_enum_params = {
    "enum_id": "STRATEGY_DCA",
    "name": "DCA Strategy",
    "description": "Dollar Cost Averaging strategy orders",
    "default_fee_rate": 0.005,
    "pair_overrides": {"PERP_BTC_USDC": 0.003},
}

broker_order_enum_filters = {
    "symbol": "PERP_BTC_USDC",
    "enum_id": "STRATEGY_DCA",
    "include_archived": True,
}

public_broker_order_enum_params = {
    "broker_id": "woofi_pro",
    "symbol": "PERP_BTC_USDC",
    "enum_id": "STRATEGY_DCA",
    "include_archived": True,
}


@mock_http_response(
    responses.GET,
    f"/v1/broker/order_enums\\?{urlencode(broker_order_enum_filters)}",
    mock_data,
    200,
)
def test_get_broker_order_enums():
    client = Client(orderly_key=orderly_key, orderly_secret=orderly_secret)
    response = client.get_broker_order_enums(**broker_order_enum_filters)
    assert response == mock_data


@mock_http_response(
    responses.GET,
    f"/v1/broker/order_enum/STRATEGY_DCA",
    mock_data,
    200,
)
def test_get_broker_order_enum():
    client = Client(orderly_key=orderly_key, orderly_secret=orderly_secret)
    response = client.get_broker_order_enum(enum_id="STRATEGY_DCA")
    assert response == mock_data


@mock_http_response(
    responses.POST,
    f"/v1/broker/order_enum",
    mock_data,
    200,
)
def test_create_broker_order_enum():
    client = Client(orderly_key=orderly_key, orderly_secret=orderly_secret)
    response = client.create_broker_order_enum(**broker_order_enum_params)
    assert response == mock_data


@mock_http_response(
    responses.PUT,
    f"/v1/broker/order_enum/STRATEGY_DCA",
    mock_data,
    200,
)
def test_update_broker_order_enum():
    client = Client(orderly_key=orderly_key, orderly_secret=orderly_secret)
    response = client.update_broker_order_enum(
        enum_id="STRATEGY_DCA",
        name="DCA Strategy v2",
        default_fee_rate=0.006,
    )
    assert response == mock_data


@mock_http_response(
    responses.POST,
    f"/v1/broker/order_enum/archive",
    mock_data,
    200,
)
def test_archive_broker_order_enum():
    client = Client(orderly_key=orderly_key, orderly_secret=orderly_secret)
    response = client.archive_broker_order_enum(enum_id="STRATEGY_DCA")
    assert response == mock_data


@mock_http_response(
    responses.POST,
    f"/v1/broker/order_enum/unarchive",
    mock_data,
    200,
)
def test_unarchive_broker_order_enum():
    client = Client(orderly_key=orderly_key, orderly_secret=orderly_secret)
    response = client.unarchive_broker_order_enum(enum_id="STRATEGY_DCA")
    assert response == mock_data


@mock_http_response(
    responses.GET,
    f"/v1/public/broker/order_enums\\?{urlencode(public_broker_order_enum_params)}",
    mock_data,
    200,
)
def test_get_public_broker_order_enums():
    client = Client(orderly_key=orderly_key, orderly_secret=orderly_secret)
    response = client.get_public_broker_order_enums(**public_broker_order_enum_params)
    assert response == mock_data
