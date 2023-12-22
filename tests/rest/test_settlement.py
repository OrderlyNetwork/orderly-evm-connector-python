from tests.utils import mock_http_response, random_str
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

request_pnl_settle_params = {
    "brokerId": "woofi_dex",
    "chainId": 1,
    "settleNonce": 100,
    "userAddress": "test_address",
    "verifyingContract": "contract_address"
}

get_pnl_settle_history_params = {
    "start_t": 10000,
    "end_t": 10000,
    "page": 1,
    "size": 25
}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()
wallet_secret = random_str()

@mock_http_response(
    responses.GET,
    "/v1/settle_nonce",
    mock_data,
    200
)
def test_get_settle_pnl_nonce():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_settle_pnl_nonce()
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    "/v1/settle_pnl",
    mock_data,
    200
)
def test_request_pnl_settle():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
        wallet_secret=wallet_secret
    )
    response = client.request_pnl_settlement(**request_pnl_settle_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/pnl_settlement/history\\?{urlencode(get_pnl_settle_history_params)}",
    mock_data,
    200
)
def test_get_pnl_settle_history():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_pnl_settlement_history(**get_pnl_settle_history_params)
    response.should.equal(mock_data)