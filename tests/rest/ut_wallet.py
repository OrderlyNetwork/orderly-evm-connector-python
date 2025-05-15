import pytest
from orderly_evm_connector.rest import Rest as Client

def test_get_asset_history():
    client = Client(orderly_key="test_key", orderly_secret="test_secret")
    response = client.get_asset_history(
        token="USDC",
        side="DEPOSIT",
        status="COMPLETED",
        start_t=1699142400000,
        end_t=1699160400000,
        page=1,
        size=25
    )
    # 这里可以根据实际返回值进行断言
    assert response is not None

def test_internal_transfer():
    client = Client(orderly_key="test_key", orderly_secret="test_secret")
    response = client.internal_transfer(
        token="USDC",
        receiver_list=[
            {"account_id": "receiver_1", "amount": 100.0},
            {"account_id": "receiver_2", "amount": 200.0}
        ]
    )
    # 这里可以根据实际返回值进行断言
    assert response is not None
