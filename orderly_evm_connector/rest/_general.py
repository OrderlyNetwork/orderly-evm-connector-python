from orderly_evm_connector.lib.utils import check_required_parameters


def get_system_maintenance_status(self):
    """[Public] System maintenance status

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/system_info

    Retreive the current system maintenance status of Orderly Network. A return value of status = 0 means the system is functioning properly and a return value of status = 2 means the system is under maintenance.

    https://docs-api-evm.orderly.network/#restful-api-public-system-maintenance-status
    """
    return self._request("GET", "/v1/public/system_info")


def get_faucet_usdc(self, chain_id: str, user_address: str):
    """[Public] Get faucet USDC(Testnet only)

    Receive 1,000 USDC in the Testnet environment. Each account may only use the faucet a maximum of 5 times.

    POST https://testnet-operator-evm.orderly.org/v1/faucet/usdc

    Args:
    chain_id(string): The chain ID that the test USDC should be deposited to
    user_address(string): The address of the user account

    https://docs-api-evm.orderly.network/?shell#restful-api-public-get-faucet-usdc-testnet-only
    """

    check_required_parameters([[chain_id, "chain_id"], [user_address, "user_address"]])

    self.orderly_endpoint = "https://testnet-operator-evm.orderly.org"
    payload = {
        "broker_id": "woo-dex",
        "chain_id": chain_id,
        "user_address": user_address,
    }
    self.logger.info(
        f"Receive 1,000 USDC in the Testnet environment. {self.orderly_endpoint} {payload}"
    )
    return self._request("POST", "/v1/faucet/usdc", payload=payload)


def get_exchange_info(self, symbol: str):
    """[Public] Exchange information

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/info/:symbol

    This endpoint provides all the values for the rules that an order need to fulfil in order for it to be placed successfully. The rules are defined as follows:

    Price filter

    price >= quote_min
    price <= quote_max
    (price - quote_min) % quote_tick should equal to zero
    price <= asks[0].price * (1 + price_range) when BUY
    price >= bids[0].price * (1 - price_range) when SELL
    Size filter

    base_min <= quantity <= base_max
    (quantity - base_min) % base_tick should equal to zero
    Min Notional filter

    price * quantity should greater than min_notional
    Risk Exposure filer

    Order size should be within holding threshold. See account_info

    Get available symbols that Orderly Network supports, and also send order rules for each symbol. The definition of rules can be found at Exchange Infomation

    Args:
        symbol(string)

    https://docs-api-evm.orderly.network/#restful-api-public-exchange-information
    """
    check_required_parameters([[symbol, "symbol"]])
    return self._request("GET", f"/v1/public/info/{symbol}")


def get_token_info(self):
    """[Public] Token info

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/token

    Retrives the available tokens to custody within Orderly Network.

    https://docs-api-evm.orderly.network/#restful-api-public-token-info

    """
    return self._request("GET", "/v1/public/token")


def get_available_symbols(self):
    """[Public] Available symbols

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/info

    Get available symbols that Orderly Network supports, and also send order rules for each symbol. The definition of rules can be found at Exchange Infomation

    https://docs-api-evm.orderly.network/#restful-api-public-exchange-information
    """
    return self._request("GET", "/v1/public/info")


def get_fee_futures_information(self):
    """[Public] Futures fee information

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/fee_futures/program

    Get fee information for futures trading.

    https://docs-api-evm.orderly.network/#restful-api-public-futures-fee-information
    """
    return self._request("GET", "/v1/public/fee_futures/program")


def get_leverage_configuration(self):
    """[Public] Get leverage configuration

    Limit: 10 requests per 1 second per IP address

    GET v1/public/config

    https://docs-api-evm.orderly.network/#restful-api-public-get-leverage-configuration
    """
    return self._request("GET", "/v1/public/config")


def get_user_statistics(self):
    """[Public] Get user statistics
    Limit: 10 requests per 60 seconds

    GET /v1/client/statistics

    Get statistics of the user account

    https://docs-api-evm.orderly.network/#restful-api-private-get-user-statistics

    """
    return self._sign_request("GET", "/v1/client/statistics")
