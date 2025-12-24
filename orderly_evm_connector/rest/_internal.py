from typing import Optional, Union
from orderly_evm_connector.lib.utils import check_required_parameters


def set_min_broker_tier(
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
