from tests.utils import mock_http_response, random_str, random_str_unpadded
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}


orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()
wallet_secret = random_str_unpadded()

withdraw_request_params = {
    "broker_id": "woofi_dex",
    "chain_id": 1,
    "receiver": "receiver_addr",
    "token": "test_token",
    "amount": "10",
    "withdraw_nonce": 10,
    "user_address": "user_addr",
    "verifying_contract": "contract_addr"
}

@mock_http_response(
    responses.POST,
    "/v1/withdraw_request",
    mock_data,
    200
)
def test_withdraw_request_params():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
        wallet_secret=wallet_secret
    )
    response = client.withdraw_request(**withdraw_request_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    "/v1/withdraw_nonce",
    mock_data,
    200
)
def test_get_settle_pnl_nonce():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_withdraw_nonce()
    response.should.equal(mock_data)
