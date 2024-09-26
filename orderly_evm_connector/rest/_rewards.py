from orderly_evm_connector.lib.utils import check_required_parameters


def get_parameters_of_each_epoch(self):
    """
    Get Parameters of Each Epoch of All Epochs

    Limit: 10 requests per 1 second

    GET /v1/public/trading_rewards/epoch_info

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-parameters-of-each-epoch-for-all-epochs
    """

    return self._request("GET", "/v1/public/trading_rewards/epoch_info")


def get_epochs_data(self):
    """
    Get Epochs Data

    Limit: 10 requests per 1 second

    GET /v1/public/trading_rewards/epoch_data

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-epochs-data
    """

    return self._request("GET", "/v1/public/trading_rewards/epoch_data")

def get_broker_allocation_history(self):
    """
    Get Broker Allocation History

    Limit: 10 requests per 1 second

    GET /v1/public/trading_rewards/broker_allocation_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-broker-allocation-history
    """

    return self._request("GET", "/v1/public/trading_rewards/broker_allocation_history")


def get_wallet_trading_rewards_history(self, address: str):
    """
    Get Wallet Trading Rewards History

    Limit: 10 requests per 1 second

    GET /v1/public/trading_rewards/wallet_rewards_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-wallet-trading-rewards-history
    """
    check_required_parameters([
        [address, "address"],
    ])
    payload = {
        "address": address,
    }
    return self._request("GET", "/v1/public/trading_rewards/wallet_rewards_history", payload=payload)


def get_account_trading_rewards_history(self, address: str):
    """
    Get Account Trading Rewards History

    Limit: 10 requests per 1 second

    GET /v1/public/trading_rewards/account_rewards_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-account-trading-rewards-history
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/public/trading_rewards/account_rewards_history", payload=payload)


def get_current_epoch_estimate(self, address: str):
    """
    Get Current Epoch Estimate

    Limit: 10 requests per 1 second

    GET /v1/public/trading_rewards/current_epoch_estimate

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-current-epoch-estimate
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/public/trading_rewards/current_epoch_estimate", payload=payload)


def get_current_epoch_estimate_broker(self):
    """
    Get Current Epoch Estimate by Broker

    Limit: 10 requests per 1 second

    GET /v1/public/trading_rewards/current_epoch_broker_estimate

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-current-epoch-estimate-by-broker
    """
    return self._request("GET", "/v1/public/trading_rewards/current_epoch_broker_estimate")



def get_parameters_of_each_mm_epoch(self):
    """
    Get Parameters of Each MM Epoch of All MM Epochs

    Limit: 10 requests per 1 second

    GET /v1/public/market_making_rewards/epoch_info

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-parameters-of-each-mm-epoch-for-all-mm-epochs
    """

    return self._request("GET", "/v1/public/market_making_rewards/epoch_info")


def get_wallet_group_mm_rewards_history(self, address: str, symbol: str = None):
    """
    Get Wallet Group Market Making Rewards History

    Limit: 10 requests per 1 second

    GET /v1/public/market_making_rewards/group_rewards_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-wallet-group-market-making-rewards-history
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address, "symbol": symbol}
    return self._request("GET", "/v1/public/market_making_rewards/group_rewards_history", payload=payload)


def get_market_maker_current_epoch_estimate(self, address: str):
    """
    Get Market Maker Current Epoch Estimate

    Limit: 10 requests per 1 second

    GET /v1/public/market_making_rewards/current_epoch_estimate

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-market-maker-current-epoch-estimate
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/public/market_making_rewards/current_epoch_estimate", payload=payload)


def get_wallet_staked_balance(self, address: str):
    """
    Get Wallet's Current Staked Balance

    Limit: 10 requests per 1 second

    GET /v1/staking/balance

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-wallets-current-staked-balance
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/staking/balance", payload=payload)


def get_unstake_details(self, address: str):
    """
    Get Unstake Details

    Limit: 10 requests per 1 second

    GET /v1/staking/unstake_details

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-unstaking-order-details
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/staking/unstake_details", payload=payload)



def get_staking_overview(self):
    """
    Get Wallet's Current Staked Balance

    Limit: 10 requests per 1 second

    GET /v1/staking/overview

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-staking-overview
    """
    return self._request("GET", "/v1/staking/overview")


def get_valor_batch_info(self):
    """
    Get Valor Batch Info

    Limit: 10 requests per 1 second

    GET /v1/staking/valor/batch_info

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-valor-batch-info
    """
    return self._request("GET", "/v1/staking/valor/batch_info")


def get_valor_pool_info(self):
    """
    Get Valor Pool Info

    Limit: 10 requests per 1 second

    GET /v1/staking/valor/pool_info

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-valor-pool-info
    """
    return self._request("GET", "/v1/staking/valor/pool_info")


def get_valor_redeem_info(self, address: str):
    """
    Get Valor Redeem Info

    Limit: 10 requests per 1 second

    GET /v1/staking/valor/redeem

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/get-valor-redeem-info
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/staking/valor/redeem", payload=payload)
