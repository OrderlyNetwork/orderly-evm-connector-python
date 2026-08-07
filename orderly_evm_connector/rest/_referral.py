from orderly_evm_connector.lib.utils import check_required_parameters


def create_referral_code(self, account_id: str, referral_code: str, bonus_max_rebate_rate: float,
                         bonus_referrer_rebate_rate: float, bonus_referee_rebate_rate: float):
    """
    Create Referral Code

    Limit: 1 requests per 1 second

    POST /v1/referral/create

    Args:
        account_id(string): Account ID of the referrer (required)
        referral_code(string): The referral code to create (required)
        bonus_max_rebate_rate(number): Max bonus rebate rate (required)
        bonus_referrer_rebate_rate(number): Bonus rebate rate for the referrer (required)
        bonus_referee_rebate_rate(number): Bonus rebate rate for the referee (required)

    https://docs.orderly.network/build-on-omnichain/evm-api/restful-api/private/create-referral-code
    """
    check_required_parameters(
        [[account_id, "account_id"],
         [referral_code, "referral_code"],
         [bonus_max_rebate_rate, "bonus_max_rebate_rate"],
         [bonus_referrer_rebate_rate, "bonus_referrer_rebate_rate"],
         [bonus_referee_rebate_rate, "bonus_referee_rebate_rate"]]
    )
    payload = {
        "account_id": account_id,
        "referral_code": referral_code,
        "bonus_max_rebate_rate": bonus_max_rebate_rate,
        "bonus_referrer_rebate_rate": bonus_referrer_rebate_rate,
        "bonus_referee_rebate_rate": bonus_referee_rebate_rate
    }
    return self._sign_request("POST", "/v1/referral/create", payload=payload)


def update_referral_code(self, account_id: str, referral_code: str, bonus_max_rebate_rate: float,
                         bonus_referrer_rebate_rate: float, bonus_referee_rebate_rate: float):
    """
    Update Referral Code

    Limit: 1 requests per 1 second

    POST /v1/referral/update

    Args:
        account_id(string): Account ID of the referrer (required)
        referral_code(string): The referral code to update (required)
        bonus_max_rebate_rate(number): Max bonus rebate rate (required)
        bonus_referrer_rebate_rate(number): Bonus rebate rate for the referrer (required)
        bonus_referee_rebate_rate(number): Bonus rebate rate for the referee (required)

    https://docs.orderly.network/build-on-omnichain/evm-api/restful-api/private/update-referral-code
    """
    check_required_parameters(
        [[account_id, "account_id"],
         [referral_code, "referral_code"],
         [bonus_max_rebate_rate, "bonus_max_rebate_rate"],
         [bonus_referrer_rebate_rate, "bonus_referrer_rebate_rate"],
         [bonus_referee_rebate_rate, "bonus_referee_rebate_rate"]]
    )
    payload = {
        "account_id": account_id,
        "referral_code": referral_code,
        "bonus_max_rebate_rate": bonus_max_rebate_rate,
        "bonus_referrer_rebate_rate": bonus_referrer_rebate_rate,
        "bonus_referee_rebate_rate": bonus_referee_rebate_rate
    }
    return self._sign_request("POST", "/v1/referral/update", payload=payload)


def bind_referral_code(self, referral_code: str):
    """
    Bind Referral Code

    Limit: 1 requests per 1 second

    POST /v1/referral/bind

    https://docs.orderly.network/build-on-omnichain/evm-api/restful-api/private/bind-referral-code
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

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-referral-code-info
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

    https://docs.orderly.network/build-on-omnichain/evm-api/restful-api/private/get-referral-info
    """
    return self._sign_request("GET", "/v1/referral/info")


def get_referral_history(self, start_date: str = None, end_date: str = None, page: int = None, size: int = None):
    """
    Get Referral History

    Limit: 10 requests per 1 second

    GET /v1/referral/referral_history

    https://docs.orderly.network/build-on-omnichain/evm-api/restful-api/private/get-referral-history
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
    
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-referral-rebate-summary#openapi-evmopenapi-get-v1referralrebate_summary
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

    https://docs.orderly.network/build-on-omnichain/evm-api/restful-api/private/referee_history
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

    https://docs.orderly.network/build-on-omnichain/evm-api/restful-api/private/get-referee-info
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

    https://docs.orderly.network/build-on-omnichain/evm-api/restful-api/private/get-distribution-history
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

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/check-referral-code#openapi-evmopenapi-get-v1publicreferralcheck_ref_code
    """
    check_required_parameters([[account_id,'account_id']])
    return self._request("GET", f"/v1/public/referral/check_ref_code?account_id={account_id}")

def verify_ref_code(self, referral_code:str = None ):
    """
    Verify Referral Code

    Limit: 10 requests per second 
    GET /v1/public/referral/verify_ref_code
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/verify-referral-code#openapi-evmopenapi-get-v1publicreferralverify_ref_code
    """
    check_required_parameters([[referral_code,'referral_code']])
    return self._request("GET", f"/v1/public/referral/verify_ref_code?referral_code={referral_code}")

def edit_referral_split(self, referral_code: str, bonus_referrer_rebate_rate: float,
                        bonus_referee_rebate_rate: float):
    """
    Edit Split

    Limit: 10 requests per 1 second

    POST /v1/referral/edit_split

    Args:
        referral_code(string): The referral code to edit (required)
        bonus_referrer_rebate_rate(number): Bonus rebate rate for the referrer (required)
        bonus_referee_rebate_rate(number): Bonus rebate rate for the referee (required)

    https://docs.orderly.network/build-on-omnichain/evm-api/restful-api/private/edit-split
    """
    check_required_parameters([[referral_code,'referral_code'], [bonus_referrer_rebate_rate,'bonus_referrer_rebate_rate'], [bonus_referee_rebate_rate,'bonus_referee_rebate_rate']])
    return self._sign_request("POST", "/v1/referral/edit_split", payload={
        "referral_code": referral_code,
        "bonus_referrer_rebate_rate": bonus_referrer_rebate_rate,
        "bonus_referee_rebate_rate": bonus_referee_rebate_rate
    })


def edit_referral_description(self, user_address: str, description: str = None):
    """[Private] Edit referral description

    Limit: 10 requests per 1 second

    POST /v1/referral/edit_description

    Edit the description a builder admin attaches to a referrer.

    Args:
        user_address(string): The address of the user account (required)

    Optional Args:
        description(string): Free-form description text.
    """
    check_required_parameters([[user_address, "user_address"]])
    payload = {
        "user_address": user_address,
        "description": description,
    }
    return self._sign_request("POST", "/v1/referral/edit_description", payload=payload)


def edit_referee_description(self, user_address: str, description: str = None):
    """[Private] Edit direct referee description

    Limit: 10 requests per 1 second

    POST /v1/referral/edit_referee_description

    Edit the description a builder admin attaches to a direct referee.

    Args:
        user_address(string): The address of the user account (required)

    Optional Args:
        description(string): Free-form description text.
    """
    check_required_parameters([[user_address, "user_address"]])
    payload = {
        "user_address": user_address,
        "description": description,
    }
    return self._sign_request("POST", "/v1/referral/edit_referee_description", payload=payload)


def get_auto_referral_info(self):
    """Builder admin get auto referral info
    
    Limit: 1 requests per second
    
    GET /v1/referral/auto_referral/info
    
    Scope: Only each Builder's admin wallet can call this endpoint
    
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/builder-admin-get-auto-referral-info
    """
    return self._sign_request("GET", "/v1/referral/auto_referral/info")


def get_auto_referral_progress(self):
    """Get auto referral progress
    
    Limit: 1 requests per second
    
    GET /v1/referral/auto_referral/progress
    
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-auto-referral-progress
    """
    return self._sign_request("GET", "/v1/referral/auto_referral/progress")


def update_auto_referral(self, required_trading_volume: float, max_rebate: float, referrer_rebate: float, 
                         referee_rebate: float, enable: bool, description: str = None):
    """Builder admin update auto referral
    
    Limit: 1 requests per second
    
    POST /v1/referral/auto_referral/update
    
    Scope: Only each Builder's admin wallet can call this endpoint
    
    Args:
        required_trading_volume(float): Required trading volume
        max_rebate(float): Max rebate rate
        referrer_rebate(float): Referrer rebate rate
        referee_rebate(float): Referee rebate rate
        enable(bool): Enable auto referral
        
    Optional Args:
        description(string): Description
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/builder-admin-update-auto-referral
    """
    check_required_parameters([
        [required_trading_volume, 'required_trading_volume'],
        [max_rebate, 'max_rebate'],
        [referrer_rebate, 'referrer_rebate'],
        [referee_rebate, 'referee_rebate'],
        [enable, 'enable']
    ])
    payload = {
        "required_trading_volume": required_trading_volume,
        "max_rebate": max_rebate,
        "referrer_rebate": referrer_rebate,
        "referee_rebate": referee_rebate,
        "enable": enable,
        "description": description
    }
    return self._sign_request("POST", "/v1/referral/auto_referral/update", payload=payload)


def edit_referral_code(self, current_referral_code: str, new_referral_code: str):
    """Edit Referral Code
    
    Limit: 10 requests per second
    
    POST /v1/referral/edit_referral_code
    
    Only Auto generated code can be updated
    
    Args:
        current_referral_code(string): Current referral code
        new_referral_code(string): New referral code
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/edit-referral-code
    """
    check_required_parameters([[current_referral_code, 'current_referral_code'], [new_referral_code, 'new_referral_code']])
    payload = {
        "current_referral_code": current_referral_code,
        "new_referral_code": new_referral_code
    }
    return self._sign_request("POST", "/v1/referral/edit_referral_code", payload=payload)


def get_multi_level_referral_admin_config(self):
    """[Admin] Get multilevel referral config

    Limit: 1 request per second

    GET /v1/referral/multi_level/admin

    Returns the multilevel referral configuration. Restricted to Admin users only.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-multilevel-referral-config
    """
    return self._sign_request("GET", "/v1/referral/multi_level/admin")


def get_multi_level_referral_admin_info(
    self,
    user_address: str = None,
    account_id: str = None,
    referrer_account: str = None,
    page: int = None,
    size: int = None,
    sort_by: str = None,
    level: int = None,
):
    """[Admin] Get multilevel referral info

    Limit: 10 requests per second

    GET /v1/referral/multi_level/admin/info

    Returns detailed multilevel referral information.
    Users without a created code will not appear in the response.
    Restricted to Admin users only.

    Optional Args:
        user_address(string): Only one of user_address and account_id can be provided.
        account_id(string): Only one of user_address and account_id can be provided.
        referrer_account(string): Filter by referrer account.
        page(integer): Page number.
        size(integer): Page size.
        sort_by(string): total_invites/total_traded/referee_volume/bonus_max_rebate_rate.
        level(integer): Return all if not provided.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-multilevel-referral-info
    """
    payload = {
        "user_address": user_address,
        "account_id": account_id,
        "referrer_account": referrer_account,
        "page": page,
        "size": size,
        "sort_by": sort_by,
        "level": level,
    }
    return self._sign_request("GET", "/v1/referral/multi_level/admin/info", payload=payload)


def get_multi_level_referral_admin_summary(
    self,
    start_date: str,
    end_date: str,
    aggregate_by: str = None,
    page: int = None,
    size: int = None,
    account_id: str = None,
    user_address: str = None,
    sort_by: str = None,
):
    """[Admin] Get multilevel referral summary

    Limit: 10 requests per second

    GET /v1/referral/multi_level/admin/summary

    Returns summary information for multilevel referral. Restricted to Admin users only.

    Args:
        start_date(string): Start date (YYYY-MM-DD)
        end_date(string): End date (YYYY-MM-DD)

    Optional Args:
        aggregate_by(string): Aggregation dimension (e.g. account_id/day/week/month).
        page(integer): Page number (default 1).
        size(integer): Page size.
        account_id(string): Only one of account_id and user_address can be provided.
        user_address(string): Only one of account_id and user_address can be provided.
        sort_by(string): broker_fee/total_volume/total_invites.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-multilevel-referral-summary
    """
    check_required_parameters([[start_date, "start_date"], [end_date, "end_date"]])
    payload = {
        "start_date": start_date,
        "end_date": end_date,
        "aggregate_by": aggregate_by,
        "page": page,
        "size": size,
        "account_id": account_id,
        "user_address": user_address,
        "sort_by": sort_by,
    }
    return self._sign_request("GET", "/v1/referral/multi_level/admin/summary", payload=payload)


def get_multi_level_referral_admin_referee_list(
    self,
    page: int = None,
    size: int = None,
    user_address: str = None,
    account_id: str = None,
    referrer_address: str = None,
    referrer_account: str = None,
    sort_by: str = None,
    sort_order: str = None,
):
    """[Admin] Get admin referee list

    Limit: 10 requests per second

    GET /v1/referral/multi_level/admin/referee_list

    Returns a list of referees for a builder admin.
    Includes legacy code referrals. Restricted to Admin users only.

    Optional Args:
        page(integer): Page number (default 1).
        size(integer): Page size (default 25).
        user_address(string): Only one of user_address and account_id can be provided.
        account_id(string): Only one of user_address and account_id can be provided.
        referrer_address(string): Filter by referrer address.
        referrer_account(string): Filter by referrer account id.
        sort_by(string): code_binding_time/referral_rebate_rate/referee_rebate_rate/
                         direct_invites/indirect_invites/direct_volume/indirect_volume.
        sort_order(string): ascending/descending.
    """
    payload = {
        "page": page,
        "size": size,
        "user_address": user_address,
        "account_id": account_id,
        "referrer_address": referrer_address,
        "referrer_account": referrer_account,
        "sort_by": sort_by,
        "sort_order": sort_order,
    }
    return self._sign_request(
        "GET", "/v1/referral/multi_level/admin/referee_list", payload=payload
    )


def get_multi_level_referral_statistics(self, time_range: str):
    """Get multilevel referral statistics

    Limit: 10 requests per second

    GET /v1/referral/multi_level/statistics

    Returns multilevel referral statistics for the user.

    Args:
        time_range(string): Time range (1d/7d/30d/all_time)

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-multilevel-referral-statistics
    """
    check_required_parameters([[time_range, "time_range"]])
    payload = {"time_range": time_range}
    return self._sign_request("GET", "/v1/referral/multi_level/statistics", payload=payload)


def get_multi_level_max_rebate_rate(self):
    """Get max rebate rate

    Limit: 1 request per second

    GET /v1/referral/multi_level/max_rebate_rate

    Returns the maximum rebate rate for the user in the multilevel referral program.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-max-rebate-rate
    """
    return self._sign_request("GET", "/v1/referral/multi_level/max_rebate_rate")


def get_multi_level_rebate_info(self):
    """Get multilevel rebate info

    Limit: 1 request per second

    GET /v1/referral/multi_level/rebate_info

    Returns detailed rebate information for the referral code.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-rebate-info
    """
    return self._sign_request("GET", "/v1/referral/multi_level/rebate_info")


def get_multi_level_referee_list(
    self,
    page: int = None,
    size: int = None,
    address: str = None,
    sort_by: str = None,
    sort_order: str = None,
):
    """Get multilevel referee list

    Limit: 10 requests per second

    GET /v1/referral/multi_level/referee_list

    Returns the list of direct referees (those who used your code).
    Includes both multilevel and legacy referral codes.

    Optional Args:
        page(integer): Page number (default 1).
        size(integer): Page size (default 25).
        address(string): Filter by address.
        sort_by(string): code_binding_time/referral_rebate_rate/referee_rebate_rate/
                         direct_invites/indirect_invites/direct_volume/indirect_volume.
        sort_order(string): ascending/descending.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-referee-list
    """
    payload = {
        "page": page,
        "size": size,
        "address": address,
        "sort_by": sort_by,
        "sort_order": sort_order,
    }
    return self._sign_request("GET", "/v1/referral/multi_level/referee_list", payload=payload)


def get_multi_level_volume_prerequisite(self):
    """Get multilevel volume prerequisite

    Limit: 10 requests per second

    GET /v1/referral/multi_level/volume_prerequisite

    Returns the volume prerequisite for the multilevel referral program.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-volume-prerequisite
    """
    return self._sign_request("GET", "/v1/referral/multi_level/volume_prerequisite")


def enable_multi_level_referral(self, enable: bool, base_rebate_rate: float = None,
                                default_bonus_rebate_rate: float = None,
                                required_volume: float = None):
    """[Admin] Enable or configure multilevel referral

    Limit: 1 request per second

    POST /v1/referral/multi_level/admin

    Enables or configures the multilevel referral program.
    Restricted to Admin users only.

    Args:
        enable(boolean): Enable Multi-Level Referral program

    Optional Args:
        base_rebate_rate(number): Base rebate rate applied to all affiliates.
        default_bonus_rebate_rate(number): Default bonus rebate rate.
        required_volume(number): Required volume for referral.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/enable-multilevel-referral
    """
    check_required_parameters([[enable, "enable"]])
    payload = {
        "enable": enable,
        "base_rebate_rate": base_rebate_rate,
        "default_bonus_rebate_rate": default_bonus_rebate_rate,
        "required_volume": required_volume,
    }
    return self._sign_request("POST", "/v1/referral/multi_level/admin", payload=payload)


def update_multi_level_referral_config(self, required_volume: float, base_rebate_rate: float,
                                       default_bonus_rebate_rate: float):
    """[Admin] Update multilevel referral config

    Limit: 1 request per second

    POST /v1/referral/multi_level/admin/update

    Updates the multilevel referral configuration.
    Restricted to Admin users only.

    Args:
        required_volume(number): Required volume for referral
        base_rebate_rate(number): Base rebate rate applied to all affiliates
        default_bonus_rebate_rate(number): Default bonus rebate rate

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/update-multilevel-referral-config
    """
    check_required_parameters([
        [required_volume, "required_volume"],
        [base_rebate_rate, "base_rebate_rate"],
        [default_bonus_rebate_rate, "default_bonus_rebate_rate"],
    ])
    payload = {
        "required_volume": required_volume,
        "base_rebate_rate": base_rebate_rate,
        "default_bonus_rebate_rate": default_bonus_rebate_rate,
    }
    return self._sign_request("POST", "/v1/referral/multi_level/admin/update", payload=payload)


def update_multi_level_affiliate_rebate(self, bonus_rebate_rate: float, account_ids: list):
    """[Admin] Update L1 affiliate rebate rate

    Limit: 1 request per second

    POST /v1/referral/multi_level/admin/update/affiliate

    Updates the bonus rebate rate of an L1 affiliate.
    Broker can only update the rate for L1 affiliates.
    Restricted to Admin users only.

    Args:
        bonus_rebate_rate(number): Custom bonus rebate rate for the target affiliate(s)
        account_ids(list): The L1 affiliate account(s) to update

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/update-affiliate-rebate-rate
    """
    check_required_parameters([[bonus_rebate_rate, "bonus_rebate_rate"], [account_ids, "account_ids"]])
    payload = {"bonus_rebate_rate": bonus_rebate_rate, "account_ids": account_ids}
    return self._sign_request("POST", "/v1/referral/multi_level/admin/update/affiliate", payload=payload)


def reset_multi_level_affiliate_rebate(self, account_ids: list):
    """[Admin] Reset L1 affiliate rebate rate

    Limit: 1 request per second

    POST /v1/referral/multi_level/admin/reset/affiliate

    Resets an L1 affiliate's rebate rate to default.
    Admin can only reset the rate for L1 referees.
    Restricted to Admin users only.

    Args:
        account_ids(list): The referee account(s) to reset

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/reset-affiliate-rebate-rate
    """
    check_required_parameters([[account_ids, "account_ids"]])
    if isinstance(account_ids, str):
        account_ids = [account_ids]
    payload = {"account_ids": account_ids}
    return self._sign_request("POST", "/v1/referral/multi_level/admin/reset/affiliate", payload=payload)


def create_multi_level_affiliate_code(self, account_id: str, bonus_max_rebate_rate: float,
                                      referral_code: str = None):
    """[Admin] Create multilevel referral code on affiliate's behalf

    Limit: 10 requests per second

    POST /v1/referral/multi_level/admin/create/affiliate

    Creates a multilevel referral code on an affiliate's behalf.
    Restricted to Admin users only.

    Args:
        account_id(string): The account ID to create referral code for
        bonus_max_rebate_rate(number): Maximum bonus rebate rate

    Optional Args:
        referral_code(string): The referral code to create

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/create-affiliate-code
    """
    check_required_parameters([[account_id, "account_id"], [bonus_max_rebate_rate, "bonus_max_rebate_rate"]])
    payload = {
        "account_id": account_id,
        "bonus_max_rebate_rate": bonus_max_rebate_rate,
        "referral_code": referral_code,
    }
    return self._sign_request("POST", "/v1/referral/multi_level/admin/create/affiliate", payload=payload)


def claim_multi_level_referral_code(self, bonus_referee_rebate_rate: float):
    """Claim referral code

    Limit: 1 request per second

    POST /v1/referral/multi_level/claim_code

    Claims a referral code for the user.

    Args:
        bonus_referee_rebate_rate(number): New bonus rebate rate for referees

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/claim-referral-code
    """
    check_required_parameters([[bonus_referee_rebate_rate, "bonus_referee_rebate_rate"]])
    payload = {"bonus_referee_rebate_rate": bonus_referee_rebate_rate}
    return self._sign_request("POST", "/v1/referral/multi_level/claim_code", payload=payload)


def update_multi_level_rebate_rate(self, bonus_referee_rebate_rate: float, account_ids: list = None):
    """Update referee rebate rate

    Limit: 1 request per second

    POST /v1/referral/multi_level/rebate_rate/update

    Updates the rebate rate for referees.
    Users can only update the rate for their direct referees.

    Args:
        bonus_referee_rebate_rate(number): New bonus rebate rate for referees

    Optional Args:
        account_ids(list): The referee account(s) to update.
                          Updates default rate if not provided.

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/update-rebate-rate
    """
    check_required_parameters([[bonus_referee_rebate_rate, "bonus_referee_rebate_rate"]])
    payload = {"bonus_referee_rebate_rate": bonus_referee_rebate_rate, "account_ids": account_ids}
    return self._sign_request("POST", "/v1/referral/multi_level/rebate_rate/update", payload=payload)


def set_default_multi_level_rebate_rate(self, account_ids: list):
    """Reset referee rebate rate to default

    Limit: 1 request per second

    POST /v1/referral/multi_level/rebate_rate/set_default

    Resets the referee rebate rate to default.
    Users can only reset the rate for their direct referees.

    Args:
        account_ids(list): The referee account(s) to reset

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/set-default-rebate-rate
    """
    check_required_parameters([[account_ids, "account_ids"]])
    payload = {"account_ids": account_ids}
    return self._sign_request("POST", "/v1/referral/multi_level/rebate_rate/set_default", payload=payload)


def get_referee_rebate_summary(self, start_date: str, end_date: str):
    """Get Referee Rebate Summary
    
    Limit: 10 requests per second
    
    GET /v1/referral/referee_rebate_summary
    
    Provides daily statistics on referee rebates
    
    Args:
        start_date(string): Start date (format: YYYY-MM-DD)
        end_date(string): End date (format: YYYY-MM-DD)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/get-referee-rebate-summary
    """
    check_required_parameters([[start_date, 'start_date'], [end_date, 'end_date']])
    payload = {"start_date": start_date, "end_date": end_date}
    return self._sign_request("GET", "/v1/referral/referee_rebate_summary", payload=payload)