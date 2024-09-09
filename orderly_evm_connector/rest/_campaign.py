from orderly_evm_connector.lib.utils import check_required_parameters, get_timestamp


def get_points_epoch(self):
    """[Public] Get Number of Points for Distribution

    Retrieve the number of points for past epochs and current epoch.

    GET /v1/public/points/epoch

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-number-of-epoch-points

    """

    return self._request("GET", "/v1/public/points/epoch")

def get_points_epochdates(self):
    """[Public] Get Start and End Date of All Epochs

    Limit: 10 requests per 1 second per user

    GET /v1/public/points/epoch_dates

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-start-and-end-date-of-all-epochs#openapi-evmopenapi-get-v1publicpointsepoch_dates

    """

    return self._request("GET", "/v1/public/points/epoch_dates")

def get_user_points(self,address):
    """[Public] Get User's Points

    Limit: 10 requests per 1 second per user

    GET /v1/client/points
    Args:
        address(string)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-number-of-points#openapi-evmopenapi-get-v1clientpoints
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

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-number-of-points#openapi-evmopenapi-get-v1clientpoints
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

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-campaign-user-info
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
