from orderly_evm_connector.lib.utils import check_required_parameters


def get_all_notifications(self, **kwargs):
    """[Private] Get all notifications

    Limit: 10 requests per 60 seconds

    Get all notifications for the user.

    Currently the only supported message type is the order filled message.

    GET /v1/notification/inbox/notifications

    Optional Args:
        type(string): Filter nofications by type (TRADE / SYSTEM).
        page(number): (default: 1)  the page you wish to query.
        size(number): (default: 25) the page size you wish to query. (max: 500)

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-all-notifications

    """
    payload = {**kwargs}
    return self._sign_request(
        "GET", "/v1/notification/inbox/notifications", payload=payload
    )


def get_unread_notifications(self):
    """[Private] Get unread notification information

    Limit: 10 requests per 60 seconds

    GET /v1/notification/inbox/unread

    Get the information on unread messages for the user.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-unread-notifications
    """
    return self._sign_request("GET", "/v1/notification/inbox/unread")


def set_read_status_notifications(self, flag: int, ids: list):
    """[Private] Set read status of notifications

    Limit: 10 requests per 60 seconds

    POST /v1/notification/inbox/mark_read

    Set the read status on a list of notifications for a user.

    Args:
        flag(number): The value of the read flag, where 1 = READ and 0 = UNREAD
        ids(list): The list of notification ids to flag as read/unread.

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/set-read-status-of-notifications
    """
    check_required_parameters([[flag, "flag"], [ids, "ids"]])
    payload = {"flag": flag, "ids": ids}
    return self._sign_request(
        "POST", "/v1/notification/inbox/mark_read", payload=payload
    )


def set_read_status_all_notifications(self, flag: int):
    """[Private] Set read status of all notifications

    Limit: 10 requests per 60 seconds

    POST /v1/notification/inbox/mark_read_all

    Set the read status on all notifications for a user.

    Args:
        flag(number): The value of the read flag, where 1 = READ and 0 = UNREAD

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/set-read-status-of-all-notifications
    """
    payload = {"flag": flag}
    check_required_parameters([[flag, "flag"]])
    return self._sign_request(
        "POST", "/v1/notification/inbox/mark_read_all", payload=payload
    )
