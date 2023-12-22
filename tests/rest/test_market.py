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
