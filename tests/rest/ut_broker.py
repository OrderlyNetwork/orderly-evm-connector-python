import unittest
from orderly_evm_connector.rest import Rest as Client

orderly_key = "s"
orderly_secret = "ed25519:" + "s"
orderly_account_id = "x"
wallet_secret = "x"
orderly_testnet = False

get_user_fee_rate_params = {
    "account_id": "test_account_id",
    "address": "0xaddress",
    "page": 1,
    "size": 5
}

update_user_fee_rate_params = {
    "account_ids": "test_account_id",
    "maker_fee_rate": 0.1,
    "taker_fee_rate": 0.1
}

reset_user_fee_rate_params = {
    "account_ids": ["acc1", "acc2"]
}

update_default_broker_fee_params = {
    "maker_fee_rate": 0.1,
    "taker_fee_rate": 0.1
}

get_broker_daily_volume_params = {
    "start_date": "2023-12-01",
    "end_date": "2023-12-30"
}


class AccountUnitTest(unittest.TestCase):
    def test_get_list_of_brokers(self):
        client = Client(
            orderly_key=orderly_key,
            orderly_secret=orderly_secret,
            orderly_account_id=orderly_account_id,
            wallet_secret=wallet_secret,
            orderly_testnet=orderly_testnet,
            debug=True
        )
        response = client.get_list_of_brokers()


    def test_get_broker_daily_volume(self):
        client = Client(
            orderly_key=orderly_key,
            orderly_secret=orderly_secret,
            orderly_account_id=orderly_account_id,
            wallet_secret=wallet_secret,
            orderly_testnet=orderly_testnet,
            debug=True
        )
        response = client.get_broker_daily_volume(**get_broker_daily_volume_params)


    # def test_get_user_fee_rate(self):
    #     client = Client(
    #         orderly_key=orderly_key,
    #         orderly_secret=orderly_secret,
    #         orderly_account_id=orderly_account_id,
    #         wallet_secret=wallet_secret,
    #         orderly_testnet=orderly_testnet,
    #         debug=True
    #     )
    #     response = client.get_user_fee_rates(**get_user_fee_rate_params)
    #
    #
    # def test_update_user_fee_rate(self):
    #     client = Client(
    #         orderly_key=orderly_key,
    #         orderly_secret=orderly_secret,
    #         orderly_account_id=orderly_account_id,
    #         wallet_secret=wallet_secret,
    #         orderly_testnet=orderly_testnet,
    #         debug=True
    #     )
    #     response = client.update_user_fee_rate(**update_user_fee_rate_params)
    #
    #
    # def test_reset_user_fee_rate(self):
    #     client = Client(
    #         orderly_key=orderly_key,
    #         orderly_secret=orderly_secret,
    #         orderly_account_id=orderly_account_id,
    #         wallet_secret=wallet_secret,
    #         orderly_testnet=orderly_testnet,
    #         debug=True
    #     )
    #     response = client.reset_user_fee_rate(**reset_user_fee_rate_params)
    #
    #
    # def test_update_default_broker_fee(self):
    #     client = Client(
    #         orderly_key=orderly_key,
    #         orderly_secret=orderly_secret,
    #         orderly_account_id=orderly_account_id,
    #         wallet_secret=wallet_secret,
    #         orderly_testnet=orderly_testnet,
    #         debug=True
    #     )
    #     response = client.reset_user_fee_rate(**update_default_broker_fee_params)
    #
    #
    # def test_update_default_broker_fee(self):
    #     client = Client(
    #         orderly_key=orderly_key,
    #         orderly_secret=orderly_secret,
    #         orderly_account_id=orderly_account_id,
    #         wallet_secret=wallet_secret,
    #         orderly_testnet=orderly_testnet,
    #         debug=True
    #     )
    #     response = client.reset_user_fee_rate()

if __name__ == '__main__':
    unittest.main()