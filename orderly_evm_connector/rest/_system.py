from orderly_evm_connector.lib.utils import check_required_parameters


def get_valut_balances(self, chain_id: int = None, token: str = None):
    """Get Vault Balances

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/vault_balance


    Optional Args:
        chain_id(number): id of the chain you wish to query.
        token(string): the token you wish to query

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-vault-balance
    """
    payload = {"chain_id": chain_id, "token": token}
    return self._request("GET", "/v1/public/vault_balance", payload=payload)


# def get_valut_chain_config(self, broker_id: str = None):
#     """Get vault chain config
#
#     Limit: 10 requests per 1 second per IP address
#
#     GET /v1/public/chain_info
#
#     Args:
#         broker_id: str
#
#     https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-vault-chain-config
#     """
#
#     payload = {
#         "broker_id": broker_id
#     }
#     return self._request("GET", "/v1/public/chain_info", payload=payload)

def get_supported_chains_broker(self,broker_id: str = None):
    """
    Get Supported Chains per Broker
    Limit: 10 requests per 1 second per IP address

    GET /v1/public/chain_info

    Get chains specified broker is available on.
    """
    # check_required_parameters(
    #     [[broker_id, "broker_id"]]
    # )
    payload = {"broker_id":broker_id}
    return self._request("GET", "/v1/public/chain_info",payload=payload)
