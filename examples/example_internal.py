import pprint
from orderly_evm_connector.rest import Rest as Client
from orderly_evm_connector.lib.utils import get_account_info

# 获取账户配置信息
(
    orderly_key,
    orderly_secret,
    orderly_account_id,
    wallet_secret,
    orderly_testnet,
    wss_id,
) = get_account_info('config.ini')  # 从examples目录运行时，config.ini在同目录下

# 创建私有REST客户端
client = Client(
    orderly_key=orderly_key,
    orderly_secret=orderly_secret,
    orderly_account_id=orderly_account_id,
    wallet_secret=wallet_secret,
    orderly_testnet=orderly_testnet,
    debug=True
)

def create_order():
    try:
        response = client.create_order(symbol='PERP_BTC_USDC', order_type='MARKET', side='BUY', order_quantity=0.001)
        print(response)
    except Exception as e:
        print(f"Error create_order: {e}")

def set_min_broker_tier():
    try:
        response = client.set_min_broker_tier(min_broker_tier='GOLD', account_id='0xfc7a424a383b7c4869a2ad2067dffea626b4e47fafa33d4309c8593f65ea29d6', trial=True)
        print(response)
    except Exception as e:
        print(f"Error set_min_broker_tier: {e}")

def refresh_broker_tier():
    try:
        response = client.refresh_broker_tier(broker_ids='12345')
        print(response)
    except Exception as e:
        print(f"Error create_broker: {e}")

def create_broker():
    try:
        response = client.create_broker(broker_id='12345', broker_name='Emma', min_broker_tier='Silver', default_maker_fee_rate=5, default_taker_fee_rate=10, default_rwa_maker_fee_rate=4.75, default_rwa_taker_fee_rate=9)
        print(response)
    except Exception as e:
        print(f"Error create_broker: {e}")


if __name__ == "__main__":
    # create_order()
    set_min_broker_tier()
    refresh_broker_tier()
    create_broker()