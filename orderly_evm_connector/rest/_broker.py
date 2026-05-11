from orderly_evm_connector.lib.utils import check_required_parameters


def get_list_of_brokers(self, broker_id: str = None):
    """Get list of brokers

    Limit: 10 requests per 1 second per IP address

    GET /v1/public/broker/name?broker_id=:broker_id

    Get the list of brokers currently onboarded on Orderly Network.

    Args:
        broker_id(string): If provided, it will only output details for the particular broker.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-builder-list
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

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-user-fee-rates
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

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-builders-users-volumes
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
    """Get TVL by Builder
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/balance/stats
    
    Get TVL(Total Balance + Unsettled PnL) by broker
    
    Optional Args:
        broker_id(string): Return all TVL if not specified
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-tvl-by-builder
    """
    payload = {
        "broker_id": broker_id
    }
    return self._request("GET", "/v1/public/balance/stats", payload=payload)


def get_broker_stats(self, broker_id: str = None):
    """Get Builder Stats
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/broker/stats
    
    Get the stats of a specific builder
    
    Optional Args:
        broker_id(string): If provided, it will only return details for the particular builder
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-builder-stats
    """
    payload = {
        "broker_id": broker_id
    }
    return self._request("GET", "/v1/public/broker/stats", payload=payload)


def get_broker_info(self):
    """Get broker info

    Limit: 10 requests per 60 seconds

    GET /v1/broker/broker_info

    Get broker tiered fee daily log information including staking balance,
    trading volume, and fee rates.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-broker-info
    """
    return self._sign_request("GET", "/v1/broker/broker_info")


def get_broker_order_enums(self, symbol: str = None, enum_id: str = None, include_archived: bool = None):
    """List all order enums for broker

    Limit: 10 requests per 1 second

    GET /v1/broker/order_enums

    List all order enums for the broker with usage stats.

    Optional Args:
        symbol(string): Filter by trading pair.
        enum_id(string): Filter by enum ID.
        include_archived(boolean): Include archived enums.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-order-enums-for-broker
    """
    payload = {"symbol": symbol, "enum_id": enum_id, "include_archived": include_archived}
    return self._sign_request("GET", "/v1/broker/order_enums", payload=payload)


def get_broker_order_enum(self, enum_id: str):
    """Get single order enum with stats

    Limit: 10 requests per 1 second

    GET /v1/broker/order_enum/{enum_id}

    Get a single order enum with usage stats.

    Args:
        enum_id(string): Enum ID

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-order-enum
    """
    check_required_parameters([[enum_id, "enum_id"]])
    return self._sign_request("GET", f"/v1/broker/order_enum/{enum_id}")


def create_broker_order_enum(self, **kwargs):
    """Create order enum

    Limit: 1 request per second

    POST /v1/broker/order_enum

    Create a new order enum.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/create-order-enum
    """
    payload = {**kwargs}
    return self._sign_request("POST", "/v1/broker/order_enum", payload=payload)


def update_broker_order_enum(self, enum_id: str, **kwargs):
    """Update order enum

    Limit: 1 request per second

    PUT /v1/broker/order_enum/{enum_id}

    Update an order enum. Cannot change enum_id.

    Args:
        enum_id(string): Enum ID

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/update-order-enum
    """
    check_required_parameters([[enum_id, "enum_id"]])
    payload = {**kwargs}
    return self._sign_request("PUT", f"/v1/broker/order_enum/{enum_id}", payload=payload)


def archive_broker_order_enum(self, enum_id: str):
    """Archive an order enum

    Limit: 1 request per second

    POST /v1/broker/order_enum/archive

    Archive an order enum.

    Args:
        enum_id(string): Enum ID

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/archive-order-enum
    """
    check_required_parameters([[enum_id, "enum_id"]])
    payload = {"enum_id": enum_id}
    return self._sign_request("POST", "/v1/broker/order_enum/archive", payload=payload)


def unarchive_broker_order_enum(self, enum_id: str):
    """Unarchive an order enum

    Limit: 1 request per second

    POST /v1/broker/order_enum/unarchive

    Unarchive an order enum.

    Args:
        enum_id(string): Enum ID

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/unarchive-order-enum
    """
    check_required_parameters([[enum_id, "enum_id"]])
    payload = {"enum_id": enum_id}
    return self._sign_request("POST", "/v1/broker/order_enum/unarchive", payload=payload)


def get_broker_leaderboard_daily(self, start_date: str, end_date: str, page: int = None, size: int = None, order_tag: str = None):
    """Get Builder's Leaderboard
    
    Limit: 10 requests per 60 seconds
    
    GET /v1/broker/leaderboard/daily
    
    The provided start_date/end_date has to be within a 90-day range.
    Updated hourly.
    
    Args:
        start_date(string): Format YYYY-MM-DD
        end_date(string): Format YYYY-MM-DD
        
    Optional Args:
        page(number): Start from 1
        size(number): Page size
        order_tag(string): Order tag
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-builders-leaderboard
    """
    check_required_parameters([[start_date, "start_date"], [end_date, "end_date"]])
    payload = {
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
        "size": size,
        "order_tag": order_tag
    }
    return self._sign_request("GET", "/v1/broker/leaderboard/daily", payload=payload)