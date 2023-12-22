from tests.utils import mock_http_response, random_str
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

get_positions_under_liquidation_params = {
    "start_t": 10000,
    "end_t": 10000
}

get_liquidated_positions_info_params = {
    "symbol": "PERP_NEAR_USDC",
    "start_t": 10000,
    "end_t": 10000
}

claim_liquidated_positions_params = {
    "liquidation_id": 10,
    "ratio_qty_request": 0.5
}

claim_from_insurance_fund_params = {
    "liquidation_id": 10,
    "symbol": "PERP_NEAR_USDC",
    "qty_request": 5
}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()


@mock_http_response(
    responses.GET,
    f"/v1/public/liquidation\\?{urlencode(get_positions_under_liquidation_params)}",
    mock_data,
    200
)
def test_get_positions_under_liquidation():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_positions_under_liquidation(**get_positions_under_liquidation_params)
    response.should.equal(mock_data)

@mock_http_response(
    responses.GET,
    f"/v1/public/liquidated_positions\\?{urlencode(get_liquidated_positions_info_params)}",
    mock_data,
    200
)
def test_get_liquidated_positions_info():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_liquidated_positions_info(**get_liquidated_positions_info_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/client/liquidator_liquidations\\?{urlencode(get_liquidated_positions_info_params)}",
    mock_data,
    200
)
def test_get_liquidated_positions_by_liquidator():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_liquidated_positions_by_liquidator(**get_liquidated_positions_info_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/liquidations\\?{urlencode(get_liquidated_positions_info_params)}",
    mock_data,
    200
)
def test_get_liquidated_positions_of_account():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_liquidated_positions_of_account(**get_liquidated_positions_info_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/liquidation",
    mock_data,
    200
)
def test_claim_liquidated_positions():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.claim_liquidated_positions(**claim_liquidated_positions_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/claim_insurance_fund",
    mock_data,
    200
)
def test_claim_from_insurance_fund():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.claim_from_insurance_fund(**claim_from_insurance_fund_params)
    response.should.equal(mock_data)
