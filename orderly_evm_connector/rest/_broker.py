from orderly_evm_connector.lib.utils import check_required_parameters


def get_list_of_brokers(self, broker_id: str = None):
    """Get list of brokers

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/broker/name?broker_id=:broker_id

    Get the list of brokers currently onboarded on Orderly Network.

    Args:
        broker_id(string): If provided, it will only output details for the particular broker.

    https://docs-api-evm.orderly.network/#restful-api-public-get-list-of-brokers
    """
    payload = {"broker_id": broker_id}
    return self._request("GET", "/v1/public/broker/name", payload=payload)
