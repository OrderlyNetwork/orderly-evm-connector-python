from tests.utils import mock_http_response, random_str
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

get_funding_fee_history_params = {
    "symbol": "PERP_NEAR_USDC"
}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()


@mock_http_response(
    responses.GET,
    f"/v1/funding_fee/history\\?{urlencode(get_funding_fee_history_params)}",
    mock_data,
    200
)
def test_get_funding_fee_history():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_funding_fee_history(**get_funding_fee_history_params)
    response.should.equal(mock_data)

@mock_http_response(
    responses.GET,
    f"/v1/public/fee_futures/program",
    mock_data,
    200
)
def test_get_account_info():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_fee_futures_information()
    response.should.equal(mock_data)