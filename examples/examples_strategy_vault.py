import pprint
from orderly_evm_connector.rest import Rest as Client
from utils.config import get_account_info

# 获取账户配置信息
(
    orderly_key,
    orderly_secret,
    orderly_account_id,
    wallet_secret,
    orderly_testnet,
    wss_id,
) = get_account_info()

# 创建私有REST客户端
client = Client(
    orderly_key=orderly_key,
    orderly_secret=orderly_secret,
    orderly_account_id=orderly_account_id,
    wallet_secret=wallet_secret,
    orderly_testnet=orderly_testnet,
    debug=True
)

# 示例：获取策略保险库nonce
def get_sv_nonce():
    try:
        response = client.get_strategy_vault_nonce()
        print("Strategy Vault Nonce Response:")
        pprint.pprint(response)
    except Exception as e:
        print(f"Error getting strategy vault nonce: {e}")

# 示例：提交SV操作请求
def submit_sv_operation():
    try:
        response = client.submit_sv_operation_request(
            payload_type=0,  # LP_DEPOSIT
            nonce="unique_nonce_string",
            receiver="receiver_address",
            amount="1000000000000000000",  # 1 ETH in wei
            vault_id="vault_id",
            token="ETH",
            dex_broker_id="broker_id",
            chain_id=1,
            chain_type="ethereum",
            signature="generated_signature",
            user_address="user_wallet_address",
            verifying_contract="contract_address"
        )
        print("SV Operation Request Response:")
        pprint.pprint(response)
    except Exception as e:
        print(f"Error submitting SV operation request: {e}")

# 示例：获取账户策略保险库交易历史
def get_sv_transaction_history():
    try:
        response = client.get_account_strategy_vault_transaction_history(
            vault_id="vault123",
            type="withdrawal",
            status="pending",
            start_t=1700000000000,
            end_t=1710000000000,
            page=1,
            size=25
        )
        print("Account Strategy Vault Transaction History Response:")
        pprint.pprint(response)
    except Exception as e:
        print(f"Error getting account strategy vault transaction history: {e}")

if __name__ == "__main__":
    # 提交SV操作请求
    submit_sv_operation()
    
    # 获取策略保险库nonce
    get_sv_nonce()
    
    # 获取账户策略保险库交易历史
    get_sv_transaction_history()