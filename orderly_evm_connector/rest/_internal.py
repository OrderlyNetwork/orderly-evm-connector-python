from typing import Optional, Union
from orderly_evm_connector.lib.utils import check_required_parameters


def set_min_broker_tier(
    self,
    min_broker_tier: str,
    broker_id: Optional[str] = None,
    account_id: Optional[str] = None,
    trial: Optional[bool] = False
):
    """
    Set Minimum Broker Tier for Broker or Ambassador User Account

    POST /v1/operation/min_broker_tier

    This endpoint sets the minimum fee tier for broker(s) or ambassador user account(s).
    If configured for an invitee through this endpoint, it overrides the distributor's
    tier assignment for this invitee in the Vanguard distributor programme.

    Args:
        min_broker_tier(str): Minimum fee tier
        broker_id(str, optional): For broker (either broker_id or account_id must be provided)
        account_id(str, optional): For ambassador user account (either broker_id or account_id must be provided)
        trial(bool, optional): False by default. This indicates whether the minimum tier
                              configuration includes tier assignment privilege for tiers set at Gold or above.
    """
    check_required_parameters([[min_broker_tier, "min_broker_tier"]])
    params = {
        'min_broker_tier': min_broker_tier,
        'trial': trial
    }

    # Either broker_id or account_id must be provided
    if broker_id is None and account_id is None:
        raise ValueError("Either broker_id or account_id must be provided")

    if broker_id is not None:
        params['broker_id'] = broker_id
    if account_id is not None:
        params['account_id'] = account_id

    return self._sign_request('POST', '/v1/operation/min_broker_tier', params)

def refresh_broker_tier(
    self,
    broker_ids: Optional[str] = None,
    account_ids: Optional[str] = None
):
    """
    Refresh Broker Tier

    POST /v1/operation/broker_tier_refresh

    This endpoint refreshes broker tiers for the provided broker IDs or account IDs.

    Args:
        broker_ids(str, optional): List of broker IDs, comma-separated, with a maximum of 10 broker IDs per request.
                                   Either broker_ids or account_ids must be provided.
        account_ids(str, optional): List of ambassador user account IDs, comma-separated, with a maximum of 10 broker IDs per request.
                                    Either broker_ids or account_ids must be provided.
    """
    params = {}

    # Either broker_ids or account_ids must be provided
    if broker_ids is None and account_ids is None:
        raise ValueError("Either broker_ids or account_ids must be provided")

    if broker_ids is not None:
        params['broker_ids'] = broker_ids
    if account_ids is not None:
        params['account_ids'] = account_ids

    return self._sign_request('POST', '/v1/operation/broker_tier_refresh', params)

def create_broker(
    self,
    broker_id: str,
    broker_name: str,
    min_broker_tier: str,
    default_maker_fee_rate: Union[int, float],
    default_taker_fee_rate: Union[int, float],
    default_rwa_maker_fee_rate: Union[int, float],
    default_rwa_taker_fee_rate: Union[int, float],
    base_maker_fee: Optional[Union[int, float]] = None,
    base_taker_fee: Optional[Union[int, float]] = None
):
    """
    Create a Broker ID

    POST /v1/operation/broker

    This endpoint creates a broker ID.

    Args:
        broker_id(str): Broker ID
        broker_name(str): Broker name
        default_maker_fee_rate(float): Unit in ten thousandths: 5 means 0.05%, >= public tiered fee
        default_taker_fee_rate(float): Unit in ten thousandths, consistent with SQL, >= public tiered fee
        default_rwa_maker_fee_rate(float): Unit in ten thousandths, consistent with SQL, >= base_taker_fee + 2
        default_rwa_taker_fee_rate(float): Unit in ten thousandths, consistent with SQL, >= 0
        min_broker_tier(str): Minimum broker tier (SELECT type from broker_tiered_fee_config)
        base_maker_fee(float, optional): Unit in ten thousandths, consistent with SQL. Only for custom base fee configuration
        base_taker_fee(float, optional): Unit in ten thousandths, consistent with SQL. Only for custom base fee configuration
    """
    check_required_parameters([[broker_id, "broker_id"], [broker_name, "broker_name"],
                               [min_broker_tier, "min_broker_tier"],
                               [default_maker_fee_rate, "default_maker_fee_rate"],
                               [default_taker_fee_rate, "default_taker_fee_rate"],
                               [default_rwa_maker_fee_rate, "default_rwa_maker_fee_rate"],
                               [default_rwa_taker_fee_rate, "default_rwa_taker_fee_rate"]])
    params = {
        'broker_id': broker_id,
        'broker_name': broker_name,
        'min_broker_tier': min_broker_tier,
        'default_maker_fee_rate': default_maker_fee_rate,
        'default_taker_fee_rate': default_taker_fee_rate,
        'default_rwa_maker_fee_rate': default_rwa_maker_fee_rate,
        'default_rwa_taker_fee_rate': default_rwa_taker_fee_rate
    }

    # Add optional parameters if provided
    if base_maker_fee is not None:
        params['base_maker_fee'] = base_maker_fee  # type: ignore
    if base_taker_fee is not None:
        params['base_taker_fee'] = base_taker_fee  # type: ignore

    return self._sign_request('POST', '/v1/operation/broker', params)

def bind_invitee_to_distributor(
    self,
    distributor_id: str,
    invitee_address: Optional[str] = None,
    invitee_id: Optional[str] = None
):
    """
    Bind invitee to distributor

    POST /v1/operation/orderly_one/vanguard/bind

    This endpoint binds an invitee to the distributor in the vanguard distributor programme.

    Args:
        distributor_id(str): Distributor ID
        invitee_address(str, optional): Invitee address (either invitee_address or invitee_id must be provided)
        invitee_id(str, optional): Invitee ID (either invitee_address or invitee_id must be provided)
    """
    check_required_parameters([[distributor_id, "distributor_id"]])
    params = {
        "distributor_id": distributor_id
    }

    # Either invitee_address or invitee_id must be provided
    if invitee_address is None and invitee_id is None:
        raise ValueError("Either invitee_address or invitee_id must be provided")

    if invitee_address is not None:
        params['invitee_address'] = invitee_address
    if invitee_id is not None:
        params['invitee_id'] = invitee_id

    return self._sign_request('POST', '/v1/operation/orderly_one/vanguard/bind', params)

def unbind_invitee_from_distributor(
    self,
    distributor_id: str,
    invitee_address: Optional[str] = None,
    invitee_id: Optional[str] = None,

):
    """
    Unbind invitee from distributor

    DELETE /v1/operation/orderly_one/vanguard/bind

    This endpoint unbinds an invitee from the distributor in the vanguard distributor programme.

    Args:
        distributor_id(str): Distributor ID
        invitee_address(str, optional): Invitee address (either invitee_address or invitee_id must be provided)
        invitee_id(str, optional): Invitee ID (either invitee_address or invitee_id must be provided)
    """
    check_required_parameters([[distributor_id, "distributor_id"]])
    params = {
        "distributor_id": distributor_id
    }

    # Either invitee_address or invitee_id must be provided
    if invitee_address is None and invitee_id is None:
        raise ValueError("Either invitee_address or invitee_id must be provided")

    if invitee_address is not None:
        params['invitee_address'] = invitee_address
    if invitee_id is not None:
        params['invitee_id'] = invitee_id

    return self._sign_request('DELETE', '/v1/operation/orderly_one/vanguard/bind', params)

def update_distribution_code(
    self,
    broker_id: str,
    distributor_code: str
):
    """
    Update distribution code

    POST /v1/operation/orderly_one/vanguard/update

    This endpoint updates the broker's distributor code and url.

    Args:
        broker_id(str): Broker ID
        distributor_code(str): Distributor code
    """
    check_required_parameters([[broker_id, "broker_id"], [distributor_code, "distributor_code"]])
    params = {
        'broker_id': broker_id,
        'distributor_code': distributor_code
    }

    return self._sign_request('POST', '/v1/operation/orderly_one/vanguard/update', params)

def get_distributors_invitees_list(
    self,
    broker_id: str
):
    """
    Get distributor's list of invitees

    GET /v1/operation/orderly_one/vanguard/distributors/{broker_id}/invitees

    This endpoint returns the list of broker's invitees in the vanguard distributor programme.

    Args:
        broker_id(str): Distributor's broker ID
    """
    check_required_parameters([[broker_id, "broker_id"]])
    params = {}

    return self._sign_request('GET', f'/v1/operation/orderly_one/vanguard/distributors/{broker_id}/invitees', params)

def get_list_of_distributors(
    self,
    root_broker: Optional[bool] = None
):
    """
    Get list of distributors

    GET /v1/operation/orderly_one/vanguard/distributors

    This endpoint returns the list of distributors in the vanguard distributor programme.

    Args:
        root_broker(bool, optional): True if only returning root broker
    """
    params = {}

    if root_broker is not None:
        params['root_broker'] = root_broker

    return self._sign_request('GET', '/v1/operation/orderly_one/vanguard/distributors', params)

def get_revenue_share_history(
    self,
    broker_id: str,
    page: Optional[int] = None,
    size: Optional[int] = None
):
    """
    Get revenue share history of a broker

    GET /v1/operation/orderly_one/vanguard/distributors/{broker_id}/revenue_share_history

    This endpoint returns the revenue share history of a broker in the vanguard distributor programme.

    Args:
        broker_id(str): Distributor's broker ID
        page(int, optional): The page you wish to query start from 1
        size(int, optional): The page size you wish to query (max: 500)
    """
    params = {}

    if page is not None:
        params['page'] = page
    if size is not None:
        params['size'] = size

    return self._sign_request('GET', f'/v1/operation/orderly_one/vanguard/distributors/{broker_id}/revenue_share_history', params)

def get_revenue_share_history_details(
    self,
    broker_id: Optional[str] = None,
    account_id: Optional[str] = None,
    revenue_share_id: Optional[int] = None,
    page: Optional[int] = None,
    size: Optional[int] = None
):
    """
    Get revenue share history details of a broker

    GET /v1/operation/orderly_one/vanguard/distributors/revenue_share_history_details

    This endpoint returns more details of a broker's revenue share history in the vanguard distributor programme.

    Args:
        broker_id(str, optional): Broker ID if distributor is a broker (either broker_id or account_id must be provided)
        account_id(str, optional): Account ID if distributor is an ambassador (either broker_id or account_id must be provided)
        revenue_share_id(int): Revenue share ID
        page(int, optional): The page you wish to query start from 1
        size(int, optional): The page size you wish to query (max: 500)
    """
    check_required_parameters([[broker_id, "broker_id"], [revenue_share_id, "revenue_share_id"]])
    params = {
        'broker_id': broker_id,
        'revenue_share_id': revenue_share_id
    }

    # Either broker_id or account_id must be provided
    if broker_id is None and account_id is None:
        raise ValueError("Either broker_id or account_id must be provided")

    if account_id is not None:
        params['account_id'] = account_id
    
    if page is not None:
        params['page'] = page
    if size is not None:
        params['size'] = size
    
    return self._sign_request('GET', '/v1/operation/orderly_one/vanguard/distributors/revenue_share_history_details', params)

def waive_graduation_fee(
    self,
    address: str
):
    """
    Waive graduation feee

    POST /v1/operation/orderly_one/graduation_fee_waiver

    This endpoint waives the graduation fee for an Orderly One broker. The broker must still graduate, but the fee is zero.

    Args:
        address(str): address
    """
    check_required_parameters([[address, "address"]])
    params = {
        'address': address
    }

    return self._sign_request('POST', '/v1/operation/orderly_one/graduation_fee_waiver', params)

def revoke_graduation_fee_waiver(
    self,
    address: str
):
    """
    Revoke graduation fee waiver

    DELETE /v1/operation/orderly_one/graduation_fee_waiver

    This endpoint rokes the graduation fee waiver for an Orderly One broker - only applicable to ungraduated brokers.

    Args:
        address(str): address
    """
    check_required_parameters([[address, "address"]])
    params = {
        'address': address
    }

    return self._sign_request('DELETE', '/v1/operation/orderly_one/graduation_fee_waiver', params)
