from tests.utils import mock_http_response, random_str
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

get_user_fee_rate_params = {
    "account_id": "test_account_id",
    "address": "0xaddress",
    "page": 1,
    "size": 5
}

update_user_fee_rate_params = {
    "account_ids": "test_account_id",
    "maker_fee_rate": 0.1,
    "taker_fee_rate": 0.1
}

reset_user_fee_rate_params = {
    "account_ids": ["acc1", "acc2"]
}

update_default_broker_fee_params = {
    "maker_fee_rate": 0.1,
    "taker_fee_rate": 0.1
}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()


@mock_http_response(
    responses.GET,
    f"/v1/public/broker/name",
    mock_data,
    200
)
def test_get_list_of_brokers():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_list_of_brokers()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/broker/user_info",
    mock_data,
    200
)
def test_get_user_fee_rate():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_user_fee_rates(**get_user_fee_rate_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/broker/user_info",
    mock_data,
    200
)
def test_update_user_fee_rate():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.update_user_fee_rate(**update_user_fee_rate_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/broker/fee_rate/set_default",
    mock_data,
    200
)
def test_reset_user_fee_rate():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.reset_user_fee_rate(**reset_user_fee_rate_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/broker/fee_rate/default",
    mock_data,
    200
)
def test_update_default_broker_fee():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.reset_user_fee_rate(**update_default_broker_fee_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/broker/fee_rate/default",
    mock_data,
    200
)
def test_update_default_broker_fee():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.reset_user_fee_rate()
    response.should.equal(mock_data)