from tests.utils import mock_http_response, random_str, random_str_unpadded
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

add_orderly_key_params = {
    "brokerId": "woofi_dex",
    "chainId": 1,
    "orderlyKey": "orderly_key",
    "scope": "scope_1",
    "timestamp": 1000,
    "expiration": 1000,
    "userAddress": "user_addr",
}

get_orderly_key_params = {
    "account_id": "account_id",
    "orderly_key": random_str()
}

register_params = {
    "brokerId": "woofi_dex",
    "chainId": 1,
    "registrationNonce": "nonceee",
    "userAddress": "user_addr"
}


orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()
wallet_secret = random_str_unpadded()


@mock_http_response(
    responses.GET,
    f"/v1/client/orderly_key_ip_restriction\\?orderly_key={orderly_key}",
    mock_data,
    200
)
def test_get_orderly_key_ip_restrictions():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_orderlykey_ip_restriction(orderly_key=orderly_key)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/client/set_orderly_key_ip_restriction",
    mock_data,
    200
)
def test_set_orderly_key_ip_restrictions():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.set_orderlykey_ip_restriction(orderly_key=orderly_key, ip_restriction_list=[1,2,3,4])
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/client/reset_orderly_key_ip_restriction",
    mock_data,
    200
)
def test_reset_orderly_key_ip_restrictions():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.reset_orderlykey_ip_restriction(orderly_key=orderly_key, reset_mode="ALLOW_ALL_IPS")
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/client/key_info",
    mock_data,
    200
)
def test_get_current_orderly_key_ip_restrictions():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_current_orderlykey_info()
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/register_account",
    mock_data,
    200
)
def test_register_account():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.register_account(**register_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    "/v1/registration_nonce",
    mock_data,
    200
)
def test_get_registration_nonce():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_registration_nonce()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    "/v1/get_orderly_key",
    mock_data,
    200
)
def test_get_orderly_key():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_orderly_key(**get_orderly_key_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    "/v1/orderly_key",
    mock_data,
    200
)
def test_add_orderly_key():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.add_orderly_key(**add_orderly_key_params)
    response.should.equal(mock_data)