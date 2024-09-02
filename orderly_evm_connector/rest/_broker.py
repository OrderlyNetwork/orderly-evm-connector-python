from orderly_evm_connector.lib.utils import check_required_parameters


def get_list_of_brokers(self, broker_id: str = None):
    """Get list of brokers

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/broker/name?broker_id=:broker_id

    Get the list of brokers currently onboarded on Orderly Network.

    Args:
        broker_id(string): If provided, it will only output details for the particular broker.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-broker-list
    """
    payload = {"broker_id": broker_id}
    return self._request("GET", "/v1/public/broker/name", payload=payload)

#add Get User Fee Tier API in Broker
def get_user_fee_tier(self,account_id: str = None,address: str = None,page: int = None,size: int = None):
    """Get the user fee rate information. Only address or account_id should be provided, not both.

    Limit 10 requests per 60 seconds

    GET /v1/broker/user_info
    Optional Aargs:
        account_id(string)
        
        address(string)
        
        page(number)
        
        size(number)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-user-fee-tier
    """
    payload = {"account_id": account_id,"address":address,"page":page,"size":size}
    return self._sign_request("GET", "/v1/broker/user_info", payload=payload)

def get_broker_daily_volume(
    self, 
    start_date: str,
    end_date: str,
    broker_id: str = None,
    address: str = None,
    order_tags: str = None,
    aggregateBy: str = None,
    sort: str = None
    ):
    """Get Broker Daily Volume
    Limit 10 requests per 60 seconds

    GET /v1/volume/broker/daily

    Get the daily historical breakdown of the user trading volume on specified broker.
    The provided start_date/end_date has to be within a 90-day range.

    Args:
        start_date(string): Format YYYY-MM-DD.
        end_date(string): Format YYYY-MM-DD.
    Optional Args:
        broker_id(string)
        address(string)
        order_tags(string)
        aggregateBy(string)
        sort(string)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-broker-daily-volume
    """
    check_required_parameters([[start_date, "start_date"], [end_date, "end_date"]])
    payload = {
        "start_date": start_date,
        "end_date": end_date,
        "broker_id": broker_id,
        "address": address,
        "order_tags": order_tags,
        "aggregateBy": aggregateBy,
        "sort": sort
        }
    return self._sign_request("GET", "/v1/volume/broker/daily", payload=payload)


def get_user_fee_rates(self, account_id: str = None, address: str = None, page: int = None, size: int = None):
    payload = {
        "account_id": account_id,
        "address": address,
        "page": page,
        "size": size
    }
    return self._sign_request("GET", "/v1/broker/user_info", payload=payload)


def update_user_fee_rate(self, account_ids: str, maker_fee_rate: float, taker_fee_rate: float):
    check_required_parameters(
        [[account_ids, "account_ids"],
         [maker_fee_rate, "maker_fee_rate"],
         [taker_fee_rate, "taker_fee_rate"]]
    )
    payload = {
        "account_ids": account_ids,
        "maker_fee_rate": maker_fee_rate,
        "taker_fee_rate": taker_fee_rate
    }
    return self._sign_request("POST", "/v1/broker/fee_rate/set", payload=payload)


def reset_user_fee_rate(self, account_ids: str):
    check_required_parameters(
        [[account_ids, "account_ids"]]
    )
    payload = {
        "account_ids": account_ids
    }
    return self._sign_request("POST", "/v1/broker/fee_rate/set_default", payload=payload)


def update_default_broker_fee(self, maker_fee_rate: float, taker_fee_rate: float):
    check_required_parameters(
        [[maker_fee_rate, "maker_fee_rate"],
         [taker_fee_rate, "taker_fee_rate"]]
    )
    payload = {
        "maker_fee_rate": maker_fee_rate,
        "taker_fee_rate": taker_fee_rate
    }
    return self._sign_request("POST", "/v1/broker/fee_rate/default", payload=payload)


def get_default_broker_fee(self):
    return self._sign_request("GET", "/v1/broker/fee_rate/default")


def get_tvl_by_broker(self, broker_id: str = None):
    payload = {
        "broker_id": broker_id
    }
    return self._sign_request("GET", "/v1/public/balance/stats", payload=payload)