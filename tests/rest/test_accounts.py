from tests.utils import mock_http_response, random_str
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

get_account_mock_params = {
    "address": "0x036Cb579025d3535a0ADcD929D05481a3189714b",
    "broker_id": "woofi_dex"
}
get_account_exp_params = {
    "address": "0x036Cb579025d3535a0ADcD929D05481a3189714b",
    "broker_id": "woofi_dex"
}

get_user_daily_mock_params = {
    "start_date": "2023-11-05",
    "end_date": "2023-11-06",
}
get_user_daily_exp_params = {
    "start_date": "2023-11-05",
    "end_date": "2023-11-06",
}

get_asset_hist_mock_data = {
    "token": "PERP_NEAR_USDC",
    "side": "BUY",
    "status": "FILLED",
    "start_t": 1699142400000,
    "end_t": 1699160400000
}
get_asset_hist_exp_data = {
    "token": "PERP_NEAR_USDC",
    "side": "BUY",
    "status": "FILLED",
    "start_t": 1699142400000,
    "end_t": 1699160400000
}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()


@mock_http_response(
    responses.GET,
    f"/v1/get_account\\?{urlencode(get_account_exp_params)}",
    mock_data,
    200
)
def test_get_account():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_account(**get_account_mock_params)
    response.should.equal(mock_data)

@mock_http_response(
    responses.GET,
    f"/v1/client/info",
    mock_data,
    200
)
def test_get_account_info():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_account_information()
    response.should.equal(mock_data)

@mock_http_response(
    responses.POST,
    f"/v1/client/maintenance_config",
    mock_data,
    200
)
def test_set_maintenance_config():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.set_maintenance_config(True)
    response.should.equal(mock_data)

@mock_http_response(
    responses.GET,
    f"/v1/volume/user/daily\\?{urlencode(get_user_daily_exp_params)}",
    mock_data,
    200
)
def test_get_user_daily_volume():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_user_daily_volume(**get_user_daily_mock_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/client/statistics/daily\\?{urlencode(get_user_daily_mock_params)}",
    mock_data,
    200
)
def test_get_user_daily_statistics():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_user_daily_statistics(**get_user_daily_mock_params)
    response.should.equal(mock_data)

@mock_http_response(
    responses.GET,
    f"/v1/volume/user/stats",
    mock_data,
    200
)
def test_get_user_volume_stats():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_user_volume_statistics()
    response.should.equal(mock_data)

@mock_http_response(
    responses.GET,
    f"/v1/asset/history\\?{urlencode(get_asset_hist_exp_data)}",
    mock_data,
    200
)
def test_get_asset_history():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_asset_history(**get_asset_hist_mock_data)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/account",
    mock_data,
    200
)
def test_get_account_details():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_account_details(account_id = 'test_account_id')
    response.should.equal(mock_data)

@mock_http_response(
    responses.GET,
    f"/v1/client/statistics",
    mock_data,
    200
)
def test_get_user_volume_stats():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_user_statistics()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/client/holding\\?{urlencode({'all': False})}",
    mock_data,
    200
)
def test_get_current_holdings():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_current_holdings(all=False)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/position/PERP_NEAR_USDC",
    mock_data,
    200
)
def test_get_one_position():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_one_position_info(symbol='PERP_NEAR_USDC')
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/positions",
    mock_data,
    200
)
def test_get_all_positions():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_all_positions_info()
    response.should.equal(mock_data)