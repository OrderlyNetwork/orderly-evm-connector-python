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

    return self._request("GET", f"/v1/client/points?address={address}")

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