from orderly_evm_connector.lib.utils import check_required_parameters, get_timestamp


def get_points_epoch(self):
    """[Public] Get Number of Points for Distribution

    Retrieve the number of points for past epochs and current epoch.

    GET /v1/public/points/epoch

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/get-number-of-epoch-points

    """

    return self._request("GET", "/v1/public/points/epoch")