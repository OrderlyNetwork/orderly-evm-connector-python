from orderly_evm_connector.lib.utils import check_required_parameters
def get_points_epoch(self):
    """[Public] Get Number of Points for Distribution

    Retrieve the number of points for past epochs and current epoch.

    GET /v1/public/points/epoch

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-number-of-merits-for-distribution

    """

    return self._request("GET", "/v1/public/points/epoch")

def get_points_epochdates(self):
    """[Public] Get Start and End Date of All Epochs

    Limit: 10 requests per 1 second per user

    GET /v1/public/points/epoch_dates

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-start-and-end-date-of-all-epochs#openapi-evmopenapi-get-v1publicpointsepoch_dates

    """

    return self._request("GET", "/v1/public/points/epoch_dates")

def get_user_points(self,address):
    """[Public] Get User's Points

    Limit: 10 requests per 1 second per user

    GET /v1/client/points
    Args:
        address(string)

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-users-merits#openapi-evmopenapi-get-v1clientpoints
    """
    endpoint = "/v1/client/points"
    if address:
        endpoint = endpoint + f"?address={address}"
    return self._request("GET", endpoint)

def get_points_leaderboard(self,start_r: int = None,end_r: int = None,epoch_id: int = None,page: int = None,size: int = None):
    """[Public] Get Points Leaderboard
    Limit: 10 requests per 1 second per IP address  

    GET /v1/public/points/leaderboard
    Args:
        address(string)

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-users-merits#openapi-evmopenapi-get-v1clientpoints
    """
    payload = {
        "start_r": start_r,
        "end_r": end_r,
        "epoch_id": epoch_id,
        "page": page,
        "size": size

    }
    return self._request("GET", "/v1/public/points/leaderboard",payload=payload)

def get_tradingrewards_epoch(self):
    """[Public] Get epochs data – return data of each epoch from epoch 1 to the current epoch
    Limit: 10 per second per IP address  

    GET /v1/public/tradingrewards/epoch_data

    """
    return self._request("GET", "/v1/public/tradingrewards/epoch_data")


def get_campaign_user_info(self, campaign_id: int, account_id: str = None, user_address: str = None, broker_id: str = None,
                           symbol: str = None, order_tag: str = None):
    """
    [Public] Get Campaign User Info
    Limit: 10 requests per second

    GET /v1/public/campaign/user

    Args:
        campaign_id: int
        account_id: str
        user_address: str
        broker_id: str
        symbol: str
        order_tag: str

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-campaign-user-info
    """
    payload = {
        "campaign_id": campaign_id,
        "account_id": account_id,
        "user_address": user_address,
        "broker_id": broker_id,
        "symbol": symbol,
        "order_tag": order_tag
    }
    return self._request("GET", "/v1/public/campaign/user",payload=payload)


def get_campaign_check(self, campaign_id: int, type: str, address: str, lower_boundary: int, cmp: str = None):
    """Get Campaign Verification
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/campaign/check
    
    Args:
        campaign_id(int): Campaign ID
        type(string): `volume`/`deposit`/`withdraw`/`order_count`
        address(string): User address
        lower_boundary(int): lower boundary
        
    Optional Args:
        cmp(string): cmp

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-campaign-verification
    """
    payload = {
        "campaign_id": campaign_id,
        "type": type,
        "address": address,
        "lower_boundary": lower_boundary,
        "cmp": cmp
    }
    return self._request("GET", "/v1/public/campaign/check", payload=payload)


def get_campaign_ranking(self, campaign_id: int, broker_id: str = None, page: int = None, size: int = None):
    """Get Campaign Ranking
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/campaign/ranking
    
    Args:
        campaign_id(int): Campaign ID
        
    Optional Args:
        broker_id(string): Broker ID
        page(int): Page number (start from 1)
        size(int): Page size
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-campaign-ranking
    """
    payload = {
        "campaign_id": campaign_id,
        "broker_id": broker_id,
        "page": page,
        "size": size
    }
    return self._request("GET", "/v1/public/campaign/ranking", payload=payload)


def get_campaign_stats(self, campaign_id: int, broker_id: str = None, symbol: str = None, order_tag: str = None):
    """Get Campaign Statistics
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/campaign/stats
    
    Args:
        campaign_id(int): Campaign ID
        
    Optional Args:
        broker_id(string): Broker ID
        symbol(string): Symbol
        order_tag(string): Order tag
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-campaign-statistics
    """
    payload = {
        "campaign_id": campaign_id,
        "broker_id": broker_id,
        "symbol": symbol,
        "order_tag": order_tag
    }
    return self._request("GET", "/v1/public/campaign/stats", payload=payload)


def get_campaign_stats_details(self, campaign_id: int, broker_id: str = None, symbols: str = None, group_by: str = None):
    """Get Detailed Campaign Info
    
    Limit: 10 requests per 1 minute per IP address
    
    GET /v1/public/campaign/stats/details
    
    Args:
        campaign_id(int): Campaign ID
        
    Optional Args:
        broker_id(string): Broker ID
        symbols(string): Symbols (comma separated)
        group_by(string): One of `BROKER` / `SYMBOL` / `NONE`
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-detailed-campaign-info
    """
    payload = {
        "campaign_id": campaign_id,
        "broker_id": broker_id,
        "symbols": symbols,
        "group_by": group_by
    }
    return self._request("GET", "/v1/public/campaign/stats/details", payload=payload)


def get_campaigns(self, start_t: int = None, end_t: int = None, only_show_alive: bool = None):
    """Get List of Campaigns
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/campaigns
    
    Optional Args:
        start_t(int): Start timestamp
        end_t(int): End timestamp
        only_show_alive(bool): Only show alive campaigns
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-list-of-campaigns
    """
    payload = {
        "start_t": start_t,
        "end_t": end_t,
        "only_show_alive": only_show_alive
    }
    return self._request("GET", "/v1/public/campaigns", payload=payload)


def get_client_points(self, address: str):
    """Get User's Merits
    
    Limit: 10 requests per 1 second per user
    
    GET /v1/client/points
    
    Args:
        address(string): User address
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-users-merits
    """
    check_required_parameters([[address, "address"]])
    payload = {"address": address}
    return self._request("GET", "/v1/client/points", payload=payload)


def sign_up_campaign(self, campaign_id: int):
    """Sign Up Campaign
    
    Limit: 10 requests per 1 second
    
    POST /v1/client/campaign/sign_up
    
    Args:
        campaign_id(int): Campaign ID
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/sign-up-campaign
    """
    check_required_parameters([[campaign_id, "campaign_id"]])
    payload = {"campaign_id": campaign_id}
    return self._sign_request("POST", "/v1/client/campaign/sign_up", payload=payload)
