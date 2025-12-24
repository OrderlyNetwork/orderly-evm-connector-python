import pprint
from dis import disco

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

def set_min_broker_tier(min_broker_tier, ambassador_account_id):
    try:
        response = client.set_min_broker_tier(min_broker_tier=min_broker_tier, account_id=ambassador_account_id)
        print(response)
    except Exception as e:
        print(f"Error set_min_broker_tier: {e}")

def refresh_broker_tier(broker_ids, account_ids):
    try:
        response = client.refresh_broker_tier(broker_ids=broker_ids, account_ids=account_ids)
        print(response)
    except Exception as e:
        print(f"Error create_broker: {e}")

def create_broker(broker_id, broker_name, min_broker_tier, default_maker_fee_rate, default_taker_fee_rate, default_rwa_maker_fee_rate, default_rwa_taker_fee_rate):
    try:
        response = client.create_broker(broker_id=broker_id, broker_name=broker_name, min_broker_tier=min_broker_tier,
                                        default_maker_fee_rate=default_maker_fee_rate,
                                        default_taker_fee_rate=default_taker_fee_rate,
                                        default_rwa_maker_fee_rate=default_rwa_maker_fee_rate,
                                        default_rwa_taker_fee_rate=default_rwa_taker_fee_rate)
        print(response)
    except Exception as e:
        print(f"Error create_broker: {e}")

def bind_invitee_to_distributor(distributor_id, invitee_address, invitee_id):
    try:
        response = client.bind_invitee_to_distributor(distributor_id=distributor_id, invitee_address=invitee_address,
                                                      invitee_id=invitee_id)
        print(response)
    except Exception as e:
        print(f"Error bind_invitee_to_distributor: {e}")

def unbind_invitee_from_distributor(distributor_id, invitee_address, invitee_id):
    try:
        response = client.unbind_invitee_from_distributor(distributor_id=distributor_id, invitee_address=invitee_address,
                                                          invitee_id=invitee_id)
        print(response)
    except Exception as e:
        print(f"Error unbind_invitee_from_distributor: {e}")

def update_distribution_code(broker_id, distributor_code):
    try:
        response = client.update_distribution_code(broker_id=broker_id, distributor_code=distributor_code)
        print(response)
    except Exception as e:
        print(f"Error update_distribution_code: {e}")

def get_distributors_invitees_list(broker_id):
    try:
        response = client.get_distributors_invitees_list(broker_id=broker_id)
        print(response)
    except Exception as e:
        print(f"Error get_distributors_invitees_list: {e}")


if __name__ == "__main__":
    min_broker_tier = 'DIAMOND'
    ambassador_account_id = '0xfc7a424a383b7c4869a2ad2067dffea626b4e47fafa33d4309c8593f65ea29d6'
    # # 1. Set Minimum Broker Tier for Broker or Ambassador User Account
    # set_min_broker_tier(min_broker_tier, ambassador_account_id)

    broker_ids = ''
    # # 2. Refresh Broker Tier
    # refresh_broker_tier(broker_ids, ambassador_account_id)

    # # 3. Create a Broker ID
    broker_id = '12345'
    broker_name = 'Emma'
    new_broker_min_broker_tier = 'GOLD'
    default_maker_fee_rate = 5
    default_taker_fee_rate = 10
    default_rwa_maker_fee_rate = 4
    default_rwa_taker_fee_rate = 9
    # create_broker(broker_id, broker_name, new_broker_min_broker_tier, default_maker_fee_rate, default_taker_fee_rate, default_rwa_maker_fee_rate, default_rwa_taker_fee_rate)

    # 4. Bind invitee to distributor
    # TODO: path not found
    distributor_id = 'ambassador'
    invitee_address = ''
    invitee_id = '12345'
    # bind_invitee_to_distributor(distributor_id, invitee_address, invitee_id)

    # 5. Unbind invitee from distributor
    # unbind_invitee_from_distributor(distributor_id, invitee_address, invitee_id)

    # 6. Update distribution code
    broker_id = '12345'
    distributor_code = '54321'
    update_distribution_code(broker_id, distributor_code)

    # broker_id = 'woofi_pro'
    # # 7. Get distributor's list of invitees
    # get_distributors_invitees_list(broker_id)

    # 8. Get list of distributors
    # get_list_of_distributors

    # 9. Get revenue share history of a broker
    # get_revenue_share_history

    # 10. Get revenue share history details of a broker
    # get_revenue_share_history_details