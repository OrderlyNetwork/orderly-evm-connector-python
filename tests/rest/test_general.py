from tests.utils import mock_http_response, random_str, random_str_unpadded
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

get_market_trades_params = {
    "symbol": "PERP_NEAR_USDC",
    "limit": 50
}

get_funding_rate_history_params = {
    "symbol": "PERP_NEAR_USDC"
}

get_kline_params = {
    "symbol": "PERP_NEAR_USDC",
    "type": "15m"
}

get_vault_params = {
    "chain_id": 1,
    "token": "user_token"
}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()


@mock_http_response(
    responses.GET,
    "/v1/public/chain_info",
    mock_data,
    200
)
def test_get_chain_config():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_chain_config()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    "/v1/public/config",
    mock_data,
    200
)
def test_get_leverage_configs():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_leverage_configuration()
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    "/v1/client/leverage",
    mock_data,
    200
)
def test_set_leverage_config():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.update_leverage_configuration(leverage=5)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    "/v1/public/futures/PERP_NEAR_USDC",
    mock_data,
    200
)
def test_get_futures_info_for_one_market():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_futures_info_for_one_market(symbol='PERP_NEAR_USDC')
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    "/v1/public/futures",
    mock_data,
    200
)
def test_get_futures_info_for_all_markets():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_futures_info_for_all_markets()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    "/v1/public/insurancefund",
    mock_data,
    200
)
def test_get_futures_info_for_all_markets():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_insurance_fund_info()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/vault_balance\\?{urlencode(get_vault_params)}",
    mock_data,
    200
)
def test_get_vault_balances():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_vault_balances(**get_vault_params)
    response.should.equal(mock_data)



@mock_http_response(
    responses.GET,
    f"/v1/public/vault_balance\\?{urlencode(get_kline_params)}",
    mock_data,
    200
)
def test_get_vault_balances():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_kline(**get_kline_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/funding_rate_history\\?{urlencode(get_funding_rate_history_params)}",
    mock_data,
    200
)
def test_get_vault_balances():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_funding_rate_history_for_one_market(**get_funding_rate_history_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/funding_rate/PERP_NEAR_USDC",
    mock_data,
    200
)
def test_get_predicted_funding_rate_one_market():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_predicted_funding_rate_for_one_market(symbol="PERP_NEAR_USDC")
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/funding_rates",
    mock_data,
    200
)
def test_get_predicted_funding_rate_all_market():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_predicted_funding_rate_for_all_markets()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/broker/name\\?broker_id=woofi_dex",
    mock_data,
    200
)
def test_get_brokers_list():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_list_of_brokers(broker_id="woofi_dex")
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/volume/stats",
    mock_data,
    200
)
def test_get_volume_statistics():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_volume_statistics()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/market_trades\\?{urlencode(get_market_trades_params)}",
    mock_data,
    200
)
def test_get_market_trades():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_market_trades(**get_market_trades_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/token",
    mock_data,
    200
)
def test_get_token_info():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_token_info()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/info\\?symbol=PERP_NEAR_USDC",
    mock_data,
    200
)
def test_get_token_info():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_exchange_info(symbol='PERP_NEAR_USDC')
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/public/system_info",
    mock_data,
    200
)
def test_get_system_maintenance_status():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.get_system_maintenance_status()
    response.should.equal(mock_data)