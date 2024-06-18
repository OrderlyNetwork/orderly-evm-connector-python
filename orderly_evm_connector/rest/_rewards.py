from orderly_evm_connector.lib.utils import check_required_parameters


def get_parameters_of_each_epoch(self):
    """
    Get Parameters of Each Epoch of All Epochs

    Limit: 10 requests per 1 second

    POST /v1/public/trading_rewards/epoch_info

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/create-referral-code
    """

    return self._request("GET", "/v1/public/trading_rewards/epoch_info")

def get_broker_allocation_history(self):
    """
    Get Broker Allocation History

    Limit: 10 requests per 1 second

    POST /v1/public/trading_rewards/broker_allocation_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/create-referral-code
    """

    return self._request("GET", "/v1/public/trading_rewards/broker_allocation_history")


def get_wallet_trading_rewards_history(self, address: str):
    """
    Get Wallet Trading Rewards History

    Limit: 10 requests per 1 second

    POST /v1/public/trading_rewards/wallet_rewards_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/create-referral-code
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/public/trading_rewards/wallet_rewards_history", payload=payload)


def get_account_trading_rewards_history(self, address: str):
    """
    Get Account Trading Rewards History

    Limit: 10 requests per 1 second

    POST /v1/public/trading_rewards/account_rewards_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/create-referral-code
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/public/trading_rewards/account_rewards_history", payload=payload)


def get_parameters_of_each_mm_epoch(self):
    """
    Get Parameters of Each MM Epoch of All MM Epochs

    Limit: 10 requests per 1 second

    POST /v1/public/market_making_rewards/epoch_info

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/create-referral-code
    """

    return self._request("GET", "/v1/public/trading_rewards/epoch_info")


def get_wallet_group_mm_rewards_history(self, address: str, symbol: str = None):
    """
    Get Wallet Group Market Making Rewards History

    Limit: 10 requests per 1 second

    POST /v1/public/market_making_rewards/group_rewards_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/create-referral-code
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address, "symbol": symbol}
    return self._request("GET", "/v1/public/market_making_rewards/group_rewards_history", payload=payload)


def get_wallet_staked_balance(self, address: str):
    """
    Get Wallet's Current Staked Balance

    Limit: 10 requests per 1 second

    POST /v1/staking/balance

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/create-referral-code
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/staking/balance", payload=payload)
