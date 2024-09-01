from orderly_evm_connector.lib.utils import check_required_parameters


def create_referral_code(self, account_id: str, referral_code: str, max_rebate_rate: float,
                         referrer_rebate_rate: float, referee_rebate_rate: float):
    """
    Create Referral Code

    Limit: 1 requests per 1 second

    POST /v1/referral/create

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/create-referral-code
    """
    check_required_parameters(
        [[account_id, "account_id"],
         [referral_code, "referral_code"],
         [max_rebate_rate, "max_rebate_rate"],
         [referrer_rebate_rate, "referrer_rebate_rate"],
         [referee_rebate_rate, "referee_rebate_rate"]]
    )
    payload = {
        "account_id": account_id,
        "referral_code": referral_code,
        "max_rebate_rate": max_rebate_rate,
        "referrer_rebate_rate": referrer_rebate_rate,
        "referee_rebate_rate": referee_rebate_rate
    }
    return self._sign_request("POST", "/v1/referral/create", payload=payload)


def update_referral_code(self, account_id: str, referral_code: str, max_rebate_rate: float,
                         referrer_rebate_rate: float, referee_rebate_rate: float):
    """
    Update Referral Code

    Limit: 1 requests per 1 second

    POST /v1/referral/ypdate

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/update-referral-code
    """
    check_required_parameters(
        [[account_id, "account_id"],
         [referral_code, "referral_code"],
         [max_rebate_rate, "max_rebate_rate"],
         [referrer_rebate_rate, "referrer_rebate_rate"],
         [referee_rebate_rate, "referee_rebate_rate"]]
    )
    payload = {
        "account_id": account_id,
        "referral_code": referral_code,
        "max_rebate_rate": max_rebate_rate,
        "referrer_rebate_rate": referrer_rebate_rate,
        "referee_rebate_rate": referee_rebate_rate
    }
    return self._sign_request("POST", "/v1/referral/update", payload=payload)


def bind_referral_code(self, referral_code: str):
    """
    Bind Referral Code

    Limit: 1 requests per 1 second

    POST /v1/referral/bind

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/bind-referral-code
    """
    check_required_parameters(
        [[referral_code, "referral_code"]]
    )
    payload = {
        "referral_code": referral_code
    }
    return self._sign_request("POST", "/v1/referral/bind", payload=payload)


def get_referral_code_info(self, page: int = None, size: int = None, user_address: str = None, account_id : str = None):
    """
    [Private]Get Referral Code Info
    
    Scope: Only each broker_id’s admin wallet can call this endpoint.


    Limit: 10 requests per 1 second

    GET /v1/referral/admin_info

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-referral-code-info
    """
    payload = {
        "page": page,
        "size": size,
    }
    if user_address:
        payload["user_address"] = user_address
    if account_id:
        payload["account_id"] = account_id
    return self._sign_request("GET", "/v1/referral/admin_info", payload=payload)


def get_referral_info(self):
    """
    Get Referral Info

    Limit: 10 requests per 1 second

    GET /v1/referral/info

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/get-referral-info
    """
    return self._sign_request("GET", "/v1/referral/info")


def get_referral_history(self, start_date: str = None, end_date: str = None, page: int = None, size: int = None):
    """
    Get Referral History

    Limit: 10 requests per 1 second

    GET /v1/referral/history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/get-referral-history
    """
    payload = {
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
        "size": size,
    }
    return self._sign_request("GET", "/v1/referral/referral_history", payload=payload)


def get_referral_rebate_summary(self, start_date: str = None, end_date: str = None, page: int = None, size: int = None):
    """
    Get Referral Rebate Summary

    Limit: 10 requests per 1 second

    GET /v1/referral/rebate_summary
    
    https://orderly.network/docs/build-on-evm/evm-api/restful-api/private/get-referral-rebate-summary#openapi-evmopenapi-get-v1referralrebate_summary
    """
    print(start_date,end_date)
    check_required_parameters([[start_date,"start_date"],[end_date,"end_date"]])
    payload = {
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
        "size": size,
    }
    return self._sign_request("GET", "/v1/referral/rebate_summary", payload=payload)


def get_referee_history(self, start_date: str = None, end_date: str = None, page: int = None, size: int = None):
    """
    Get Referee History

    Limit: 10 requests per 1 second

    GET /v1/referral/referee_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/referee_history
    """
    payload = {
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
        "size": size,
    }
    return self._sign_request("GET", "/v1/referral/referee_history", payload=payload)


def get_referee_info(self, sort: str = None, page: int = None, size: int = None):
    """
    Get Referee Info

    Limit: 10 requests per 1 second

    GET /v1/referral/referee_info

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/get-referee-info
    """
    payload = {
        "sort": sort,
        "page": page,
        "size": size,
    }
    return self._sign_request("GET", "/v1/referral/referee_info", payload=payload)


def get_distribution_history(self, start_t: str = None, end_t: str = None, page: int = None, size: int = None,type: str = None, status: str = None):
    """
    Get Distribution History

    Limit: 1 requests per 1 second

    GET /v1/client/distribution_history

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/get-distribution-history
    """
    payload = {
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size,
        "type": type,
        "status": status
    }
    return self._sign_request("GET", "/v1/client/distribution_history", payload=payload)


def check_ref_code(self, account_id:str = None ):
    """
    Check Referral Code

    Limit: 10 requests per second 
    GET /v1/public/referral/check_ref_code

    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/check-referral-code#openapi-evmopenapi-get-v1publicreferralcheck_ref_code
    """
    check_required_parameters([[account_id,'account_id']])
    return self._request("GET", f"/v1/public/referral/check_ref_code?account_id={account_id}")

def verify_ref_code(self, referral_code:str = None ):
    """
    Verify Referral Code

    Limit: 10 requests per second 
    GET /v1/public/referral/verify_ref_code
    https://orderly.network/docs/build-on-evm/evm-api/restful-api/public/verify-referral-code#openapi-evmopenapi-get-v1publicreferralverify_ref_code
    """
    check_required_parameters([[referral_code,'referral_code']])
    return self._request("GET", f"/v1/public/referral/verify_ref_code?referral_code={referral_code}")

def edit_referral_split(self, referral_code: str, referrer_rebate_rate: float, referee_rebate_rate: float):
    """
    Edit Split

    Limit: 10 requests per 1 second

    POST /v1/referral/edit_split

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/private/edit-split
    """
    check_required_parameters([[referral_code,'referral_code'], [referrer_rebate_rate,'referrer_rebate_rate'], [referee_rebate_rate,'referee_rebate_rate']])
    return self._sign_request("POST", "/v1/referral/edit_split", payload={
        "referral_code": referral_code,
        "referrer_rebate_rate": referrer_rebate_rate,
        "referee_rebate_rate": referee_rebate_rate
    })