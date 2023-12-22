from orderly_evm_connector.lib.utils import check_required_parameters


def get_valut_balances(self, chain_id: int = None, token: str = None):
    """Get Vault Balances

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/vault_balance


    Optional Args:
        chain_id(number): id of the chain you wish to query.
        token(string): the token you wish to query

    https://docs-api-evm.orderly.network/#restful-api-public-get-list-of-brokers
    """
    payload = {"chain_id": chain_id, "token": token}
    return self._request("GET", "/v1/public/vault_balance", payload=payload)


def get_valut_chain_config(self):
    """Get vault chain config

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/chain_info

    https://docs-api-evm.orderly.network/#restful-api-public-get-vault-chain-config
    """
    return self._request("GET", "/v1/public/chain_info")
