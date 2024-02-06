from tests.utils import mock_http_response, random_str
from orderly.rest import Rest as Client
from urllib.parse import urlencode
import responses

mock_data = {"key_1": "value_1", "key_2": "value_2"}

delegate_signer_params = {
    "delegateContract": "0xcontract",
    "brokerId": "woofi_pro",
    "chainId": 1,
    "timestamp": 111,
    "registrationNonce": 111,
    "txHash": "somehash",
    "userAddress": "useraddress"
}

delegate_add_orderly_key_params = {
    "delegateContract": "0xcontract",
    "brokerId": "woofi_pro",
    "chainId": 1,
    "orderlyKey": "key",
    "scope": "trading, read",
    "timestamp": 111,
    "expiration": 150,
    "userAddress": "user_address"
}

delegate_withdraw_request_params = {
    "delegateContract": "0xcontract",
    "brokerId": "woofi_pro",
    "chainId": 1,
    "receiver": "receiver_addr",
    "token": "USDC",
    "amount": 150,
    "withdrawNonce": 1,
    "timestamp": 111,
    "userAddress": "user_addr"
}

delegate_settle_pnl_params = {
    "delegateContract": "0xcontract",
    "brokerId": "woofi_pro",
    "chainId": 1,
    "settleNonce": 1,
    "timestamp": 111,
    "userAddress": "user_addr"
}

orderly_key = random_str()
orderly_secret = "ed25519:" + random_str()


@mock_http_response(
    responses.POST,
    f"/v1/delegate_signer",
    mock_data,
    200
)
def test_delegate_signer():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.delegate_signer(**delegate_signer_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/delegate_orderly_key",
    mock_data,
    200
)
def test_delegate_add_orderly_key():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.delegate_add_orderly_key(**delegate_add_orderly_key_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/delegate_withdraw_request",
    mock_data,
    200
)
def test_delegate_withdraw_request():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.delegate_withdraw_request(**delegate_withdraw_request_params)
    response.should.equal(mock_data)


@mock_http_response(
    responses.POST,
    f"/v1/delegate_settle_pnl",
    mock_data,
    200
)
def test_delegate_request_pnl_settlement():
    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
    )
    response = client.delegate_request_pnl_settlement(**delegate_settle_pnl_params)
    response.should.equal(mock_data)