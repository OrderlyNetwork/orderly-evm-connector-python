from tests.utils import mock_http_response, random_str
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

create_referral_code_params = {
    "account_id": "test_acc",
    "referral_code": "test_code",
    "bonus_max_rebate_rate": 0.1,
    "bonus_referrer_rebate_rate": 0.1,
    "bonus_referee_rebate_rate": 0.1
}

update_referral_code_params = {
    "account_id": "test_acc",
    "referral_code": "test_code",
    "bonus_max_rebate_rate": 0.1,
    "bonus_referrer_rebate_rate": 0.1,
    "bonus_referee_rebate_rate": 0.1
}

bind_referral_code_params = {
    "referral_code": "test_code",
}

get_referral_code_info_params = {
    "page": 1,
    "size": 5
}

get_referral_history_params = {
    "start_date": "date",
    "end_date": "date",
    "page": 1,
    "size": 5
}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()


@mock_http_response(
    responses.POST,
    f"/v1/referral/create",
    mock_data,
    200
)
def test_create_referral_code():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.create_referral_code(**create_referral_code_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/referral/update",
    mock_data,
    200
)
def test_update_referral_code():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.update_referral_code(**update_referral_code_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/referral/bind",
    mock_data,
    200
)
def test_bind_referral_code():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.bind_referral_code(**bind_referral_code_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/referral/admin_info",
    mock_data,
    200
)
def test_get_referral_code_info():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_referral_code_info(**get_referral_code_info_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/referral/info",
    mock_data,
    200
)
def test_get_referral_info():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_referral_info()
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/referral/referral_history",
    mock_data,
    200
)
def test_get_referral_history():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_referral_history(**get_referral_history_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/referral/rebate_summary",
    mock_data,
    200
)
def test_get_referral_rebate_summary():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_referral_rebate_summary(**get_referral_history_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/referral/referee_history",
    mock_data,
    200
)
def test_get_referee_history():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_referee_history(**get_referral_history_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/referral/referee_info",
    mock_data,
    200
)
def test_get_referee_info():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_referee_info(**get_referral_code_info_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.GET,
    f"/v1/client/distribution_history",
    mock_data,
    200
)
def test_get_distribution_history():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.get_distribution_history(**get_referral_history_params)
    response.should.equal(mock_data)

@mock_http_response(
    responses.POST,
    "/v1/referral/edit_split",
    mock_data,
    200
)
def test_edit_referral_split():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.edit_referral_split(
        referral_code="test_code",
        bonus_referrer_rebate_rate=0.1,
        bonus_referee_rebate_rate=0.05
    )
    assert response == mock_data


@mock_http_response(
    responses.POST,
    "/v1/referral/edit_description",
    mock_data,
    200
)
def test_edit_referral_description():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.edit_referral_description(
        user_address="0x036Cb579025d3535a0ADcD929D05481a3189714b",
        description="vip affiliate"
    )
    assert response == mock_data


@mock_http_response(
    responses.POST,
    "/v1/referral/edit_referee_description",
    mock_data,
    200
)
def test_edit_referee_description():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.edit_referee_description(
        user_address="0x036Cb579025d3535a0ADcD929D05481a3189714b"
    )
    assert response == mock_data


@mock_http_response(
    responses.POST,
    "/v1/referral/multi_level/admin/update",
    mock_data,
    200
)
def test_update_multi_level_referral_config():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.update_multi_level_referral_config(
        required_volume=10000,
        base_rebate_rate=0.2,
        default_bonus_rebate_rate=0.05
    )
    assert response == mock_data


@mock_http_response(
    responses.POST,
    "/v1/referral/multi_level/rebate_rate/update",
    mock_data,
    200
)
def test_update_multi_level_rebate_rate():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret
    )
    response = client.update_multi_level_rebate_rate(bonus_referee_rebate_rate=0.05)
    assert response == mock_data
