import types

import aiohttp
from asgiref.sync import sync_to_async

from orderly_evm_connector.api import API
from orderly_evm_connector.async_api import AsyncAPI


class Rest(API):
    def __init__(
        self,
        orderly_key=None,
        orderly_secret=None,
        wallet_secret=None,
        orderly_testnet=False,
        **kwargs
    ):
        self.orderly_testnet = orderly_testnet
        super().__init__(
            orderly_key, orderly_secret, wallet_secret, orderly_testnet, **kwargs
        )

    # account
    from orderly_evm_connector.rest._account import remove_orderly_key
    from orderly_evm_connector.rest._account import remove_orderly_key
    from orderly_evm_connector.rest._account import get_registration_nonce
    from orderly_evm_connector.rest._account import get_account_details
    from orderly_evm_connector.rest._account import get_account
    from orderly_evm_connector.rest._account import get_broker
    from orderly_evm_connector.rest._account import register_account
    from orderly_evm_connector.rest._account import get_orderly_key
    from orderly_evm_connector.rest._account import add_orderly_key
    from orderly_evm_connector.rest._account import update_leverage_configuration
    from orderly_evm_connector.rest._account import get_current_holdings
    from orderly_evm_connector.rest._account import get_account_information
    from orderly_evm_connector.rest._account import set_maintenance_config
    from orderly_evm_connector.rest._account import get_user_daily_statistics
    from orderly_evm_connector.rest._account import get_user_daily_volume
    from orderly_evm_connector.rest._account import get_user_volume_statistics
    from orderly_evm_connector.rest._account import get_current_orderlykey_info
    from orderly_evm_connector.rest._account import get_orderlykey_ip_restriction
    from orderly_evm_connector.rest._account import set_orderlykey_ip_restriction
    from orderly_evm_connector.rest._account import reset_orderlykey_ip_restriction
    from orderly_evm_connector.rest._broker import get_default_broker_fee
    from orderly_evm_connector.rest._broker import update_user_fee_rate
    from orderly_evm_connector.rest._broker import reset_user_fee_rate
    from orderly_evm_connector.rest._broker import update_default_broker_fee
    from orderly_evm_connector.rest._account import get_position_history

    # broker
    from orderly_evm_connector.rest._broker import get_list_of_brokers
    from orderly_evm_connector.rest._broker import get_user_fee_tier
    from orderly_evm_connector.rest._broker import get_broker_daily_volume
    from orderly_evm_connector.rest._broker import get_default_broker_fee
    from orderly_evm_connector.rest._broker import update_user_fee_rate
    from orderly_evm_connector.rest._broker import reset_user_fee_rate
    from orderly_evm_connector.rest._broker import update_default_broker_fee
    from orderly_evm_connector.rest._broker import get_tvl_by_broker

    # general
    from orderly_evm_connector.rest._general import get_system_maintenance_status
    from orderly_evm_connector.rest._general import get_faucet_usdc
    from orderly_evm_connector.rest._general import get_exchange_info
    from orderly_evm_connector.rest._general import get_token_info
    from orderly_evm_connector.rest._general import get_available_symbols
    from orderly_evm_connector.rest._general import get_fee_futures_information
    from orderly_evm_connector.rest._general import get_leverage_configuration
    from orderly_evm_connector.rest._general import get_user_statistics
    from orderly_evm_connector.rest._general import get_market_volume_by_broker

    # liquidation
    from orderly_evm_connector.rest._liquidation import get_positions_under_liquidation
    from orderly_evm_connector.rest._liquidation import get_liquidated_positions_info
    from orderly_evm_connector.rest._liquidation import get_insurance_fund_info
    from orderly_evm_connector.rest._liquidation import (
        get_liquidated_positions_by_liquidator,
    )
    from orderly_evm_connector.rest._liquidation import (
        get_liquidated_positions_of_account,
    )
    from orderly_evm_connector.rest._liquidation import claim_liquidated_positions
    from orderly_evm_connector.rest._liquidation import claim_from_insurance_fund

    # market
    from orderly_evm_connector.rest._market import get_market_trades
    from orderly_evm_connector.rest._market import get_volume_statistics
    from orderly_evm_connector.rest._market import (
        get_predicted_funding_rate_for_all_markets,
    )
    from orderly_evm_connector.rest._market import (
        get_predicted_funding_rate_for_one_market,
    )
    from orderly_evm_connector.rest._market import (
        get_funding_rate_history_for_one_market,
    )
    from orderly_evm_connector.rest._market import get_futures_info_for_all_markets
    from orderly_evm_connector.rest._market import get_futures_info_for_one_market
    from orderly_evm_connector.rest._market import get_tradingview_configuration
    from orderly_evm_connector.rest._market import get_tradingview_history_basrs
    from orderly_evm_connector.rest._market import get_tradingview_symbol_info
    from orderly_evm_connector.rest._market import get_orderbook_snapshot
    from orderly_evm_connector.rest._market import get_kline

    # notifications
    from orderly_evm_connector.rest._notifications import get_all_notifications
    from orderly_evm_connector.rest._notifications import get_unread_notifications
    from orderly_evm_connector.rest._notifications import set_read_status_notifications
    from orderly_evm_connector.rest._notifications import (
        set_read_status_all_notifications,
    )

    # system
    from orderly_evm_connector.rest._system import get_valut_balances
    # from orderly_evm_connector.rest._system import get_valut_chain_config
    from orderly_evm_connector.rest._system import get_supported_chains_broker

    # settlement
    from orderly_evm_connector.rest._settlement import get_settle_pnl_nonce
    from orderly_evm_connector.rest._settlement import request_pnl_settlement
    from orderly_evm_connector.rest._settlement import get_pnl_settlement_history

    # trade
    from orderly_evm_connector.rest._trade import create_algo_order
    from orderly_evm_connector.rest._trade import create_order
    from orderly_evm_connector.rest._trade import batch_create_order
    from orderly_evm_connector.rest._trade import edit_algo_order
    from orderly_evm_connector.rest._trade import edit_order
    from orderly_evm_connector.rest._trade import cancel_algo_order
    from orderly_evm_connector.rest._trade import cancel_algo_all_pending_order
    from orderly_evm_connector.rest._trade import cancel_order
    from orderly_evm_connector.rest._trade import cancel_algo_order_by_client_order_id
    from orderly_evm_connector.rest._trade import cancel_order_by_client_order_id
    from orderly_evm_connector.rest._trade import cancel_orders
    from orderly_evm_connector.rest._trade import batch_cancel_orders
    from orderly_evm_connector.rest._trade import batch_cancel_orders_by_client_order_id
    from orderly_evm_connector.rest._trade import get_algo_order
    from orderly_evm_connector.rest._trade import get_algo_orders
    from orderly_evm_connector.rest._trade import get_order
    from orderly_evm_connector.rest._trade import get_algo_order_by_client_order_id
    from orderly_evm_connector.rest._trade import get_order_by_client_order_id
    from orderly_evm_connector.rest._trade import get_orders
    from orderly_evm_connector.rest._trade import get_all_trades_of_order
    from orderly_evm_connector.rest._trade import get_trades
    from orderly_evm_connector.rest._trade import get_trade
    from orderly_evm_connector.rest._trade import get_all_positions_info
    from orderly_evm_connector.rest._trade import get_one_position_info
    from orderly_evm_connector.rest._trade import get_funding_fee_history

    # wallet
    from orderly_evm_connector.rest._wallet import get_asset_history
    from orderly_evm_connector.rest._wallet import get_withdraw_nonce
    from orderly_evm_connector.rest._wallet import withdraw_request
    #campaign
    from orderly_evm_connector.rest._campaign import get_points_epoch
    from orderly_evm_connector.rest._campaign import get_points_epochdates
    from orderly_evm_connector.rest._campaign import get_user_points
    from orderly_evm_connector.rest._campaign import get_points_leaderboard
    from orderly_evm_connector.rest._campaign import get_tradingrewards_epoch
    from orderly_evm_connector.rest._campaign import get_campaign_user_info
    #referral
    from orderly_evm_connector.rest._referral import bind_referral_code
    from orderly_evm_connector.rest._referral import get_referral_history
    from orderly_evm_connector.rest._referral import bind_referral_code
    from orderly_evm_connector.rest._referral import get_referral_history
    from orderly_evm_connector.rest._referral import get_referral_code_info
    from orderly_evm_connector.rest._referral import get_distribution_history
    from orderly_evm_connector.rest._referral import check_ref_code
    from orderly_evm_connector.rest._referral import verify_ref_code
    from orderly_evm_connector.rest._referral import get_referral_rebate_summary
    from orderly_evm_connector.rest._referral import get_referral_info
    from orderly_evm_connector.rest._referral import get_referee_info
    from orderly_evm_connector.rest._referral import get_referee_history
    from orderly_evm_connector.rest._referral import edit_referral_split
    from orderly_evm_connector.rest._referral import create_referral_code
    from orderly_evm_connector.rest._referral import update_referral_code
    from orderly_evm_connector.rest._referral import get_referral_info
    from orderly_evm_connector.rest._referral import get_referee_info
    from orderly_evm_connector.rest._referral import get_referee_history
    from orderly_evm_connector.rest._referral import create_referral_code
    from orderly_evm_connector.rest._referral import update_referral_code
    # rewards
    from orderly_evm_connector.rest._rewards import get_parameters_of_each_epoch
    from orderly_evm_connector.rest._rewards import get_broker_allocation_history
    from orderly_evm_connector.rest._rewards import get_account_trading_rewards_history
    from orderly_evm_connector.rest._rewards import get_wallet_trading_rewards_history
    from orderly_evm_connector.rest._rewards import get_epochs_data
    from orderly_evm_connector.rest._rewards import get_current_epoch_estimate
    from orderly_evm_connector.rest._rewards import get_current_epoch_estimate_broker
    from orderly_evm_connector.rest._rewards import get_parameters_of_each_mm_epoch
    from orderly_evm_connector.rest._rewards import get_wallet_group_mm_rewards_history
    from orderly_evm_connector.rest._rewards import get_market_maker_current_epoch_estimate
    from orderly_evm_connector.rest._rewards import get_wallet_staked_balance
    from orderly_evm_connector.rest._rewards import get_staking_overview
    from orderly_evm_connector.rest._rewards import get_unstake_details
    from orderly_evm_connector.rest._rewards import get_valor_batch_info
    from orderly_evm_connector.rest._rewards import get_valor_pool_info
    from orderly_evm_connector.rest._rewards import get_valor_redeem_info
    from orderly_evm_connector.rest._rewards import get_wallet_trading_rewards_history


class RestAsync(AsyncAPI):
    def __init__(
        self,
        orderly_key=None,
        orderly_secret=None,
        wallet_secret=None,
        orderly_testnet=False,
        **kwargs
    ):
        self.orderly_testnet = orderly_testnet
        super().__init__(
            orderly_key, orderly_secret, wallet_secret, orderly_testnet, **kwargs
        )

    # account
    from orderly_evm_connector.rest._account import get_registration_nonce
    from orderly_evm_connector.rest._account import get_account_details
    from orderly_evm_connector.rest._account import get_account
    from orderly_evm_connector.rest._account import get_broker
    from orderly_evm_connector.rest._account import register_account
    from orderly_evm_connector.rest._account import get_orderly_key
    from orderly_evm_connector.rest._account import add_orderly_key
    from orderly_evm_connector.rest._account import update_leverage_configuration
    from orderly_evm_connector.rest._account import get_current_holdings
    from orderly_evm_connector.rest._account import get_account_information
    from orderly_evm_connector.rest._account import set_maintenance_config
    from orderly_evm_connector.rest._account import get_user_daily_statistics
    from orderly_evm_connector.rest._account import get_user_daily_volume
    from orderly_evm_connector.rest._account import get_user_volume_statistics
    from orderly_evm_connector.rest._account import get_current_orderlykey_info
    from orderly_evm_connector.rest._account import get_orderlykey_ip_restriction
    from orderly_evm_connector.rest._account import set_orderlykey_ip_restriction
    from orderly_evm_connector.rest._account import reset_orderlykey_ip_restriction
    from orderly_evm_connector.rest._account import get_position_history

    from orderly_evm_connector.rest._broker import get_default_broker_fee
    from orderly_evm_connector.rest._broker import update_user_fee_rate
    from orderly_evm_connector.rest._broker import reset_user_fee_rate
    from orderly_evm_connector.rest._broker import update_default_broker_fee
    from orderly_evm_connector.rest._account import remove_orderly_key

    # broker
    from orderly_evm_connector.rest._broker import get_list_of_brokers
    from orderly_evm_connector.rest._broker import get_user_fee_tier
    from orderly_evm_connector.rest._broker import get_broker_daily_volume

    # general
    from orderly_evm_connector.rest._general import get_system_maintenance_status
    from orderly_evm_connector.rest._general import get_faucet_usdc
    from orderly_evm_connector.rest._general import get_exchange_info
    from orderly_evm_connector.rest._general import get_token_info
    from orderly_evm_connector.rest._general import get_available_symbols
    from orderly_evm_connector.rest._general import get_fee_futures_information
    from orderly_evm_connector.rest._general import get_leverage_configuration
    from orderly_evm_connector.rest._general import get_user_statistics

    # liquidation
    from orderly_evm_connector.rest._liquidation import get_positions_under_liquidation
    from orderly_evm_connector.rest._liquidation import get_liquidated_positions_info
    from orderly_evm_connector.rest._liquidation import get_insurance_fund_info
    from orderly_evm_connector.rest._liquidation import (
        get_liquidated_positions_by_liquidator,
    )
    from orderly_evm_connector.rest._liquidation import (
        get_liquidated_positions_of_account,
    )
    from orderly_evm_connector.rest._liquidation import claim_liquidated_positions
    from orderly_evm_connector.rest._liquidation import claim_from_insurance_fund

    # market
    from orderly_evm_connector.rest._market import get_market_trades
    from orderly_evm_connector.rest._market import get_volume_statistics
    from orderly_evm_connector.rest._market import (
        get_predicted_funding_rate_for_all_markets,
    )
    from orderly_evm_connector.rest._market import (
        get_predicted_funding_rate_for_one_market,
    )
    from orderly_evm_connector.rest._market import (
        get_funding_rate_history_for_one_market,
    )
    from orderly_evm_connector.rest._market import get_futures_info_for_all_markets
    from orderly_evm_connector.rest._market import get_futures_info_for_one_market
    from orderly_evm_connector.rest._market import get_tradingview_configuration
    from orderly_evm_connector.rest._market import get_tradingview_history_basrs
    from orderly_evm_connector.rest._market import get_tradingview_symbol_info
    from orderly_evm_connector.rest._market import get_orderbook_snapshot
    from orderly_evm_connector.rest._market import get_kline

    # notifications
    from orderly_evm_connector.rest._notifications import get_all_notifications
    from orderly_evm_connector.rest._notifications import get_unread_notifications
    from orderly_evm_connector.rest._notifications import set_read_status_notifications
    from orderly_evm_connector.rest._notifications import (
        set_read_status_all_notifications,
    )

    # system
    from orderly_evm_connector.rest._system import get_valut_balances
    from orderly_evm_connector.rest._system import get_supported_chains_broker

    # settlement
    from orderly_evm_connector.rest._settlement import get_settle_pnl_nonce
    from orderly_evm_connector.rest._settlement import request_pnl_settlement
    from orderly_evm_connector.rest._settlement import get_pnl_settlement_history

    # trade
    from orderly_evm_connector.rest._trade import create_algo_order
    from orderly_evm_connector.rest._trade import create_order
    from orderly_evm_connector.rest._trade import batch_create_order
    from orderly_evm_connector.rest._trade import edit_algo_order
    from orderly_evm_connector.rest._trade import edit_order
    from orderly_evm_connector.rest._trade import cancel_algo_order
    from orderly_evm_connector.rest._trade import cancel_algo_all_pending_order
    from orderly_evm_connector.rest._trade import cancel_order
    from orderly_evm_connector.rest._trade import cancel_algo_order_by_client_order_id
    from orderly_evm_connector.rest._trade import cancel_order_by_client_order_id
    from orderly_evm_connector.rest._trade import cancel_orders
    from orderly_evm_connector.rest._trade import batch_cancel_orders
    from orderly_evm_connector.rest._trade import batch_cancel_orders_by_client_order_id
    from orderly_evm_connector.rest._trade import get_algo_order
    from orderly_evm_connector.rest._trade import get_algo_orders
    from orderly_evm_connector.rest._trade import get_order
    from orderly_evm_connector.rest._trade import get_algo_order_by_client_order_id
    from orderly_evm_connector.rest._trade import get_order_by_client_order_id
    from orderly_evm_connector.rest._trade import get_orders
    from orderly_evm_connector.rest._trade import get_all_trades_of_order
    from orderly_evm_connector.rest._trade import get_trades
    from orderly_evm_connector.rest._trade import get_trade
    from orderly_evm_connector.rest._trade import get_all_positions_info
    from orderly_evm_connector.rest._trade import get_one_position_info
    from orderly_evm_connector.rest._trade import get_funding_fee_history

    # wallet
    from orderly_evm_connector.rest._wallet import get_asset_history
    from orderly_evm_connector.rest._wallet import get_withdraw_nonce
    from orderly_evm_connector.rest._wallet import withdraw_request
    # campaign
    from orderly_evm_connector.rest._campaign import get_points_epoch
    from orderly_evm_connector.rest._campaign import get_points_epochdates
    from orderly_evm_connector.rest._campaign import get_user_points
    from orderly_evm_connector.rest._campaign import get_points_leaderboard
    from orderly_evm_connector.rest._campaign import get_tradingrewards_epoch
    from orderly_evm_connector.rest._campaign import get_campaign_user_info
    # referral
    from orderly_evm_connector.rest._referral import bind_referral_code
    from orderly_evm_connector.rest._referral import get_referral_history
    from orderly_evm_connector.rest._referral import get_referral_code_info
    from orderly_evm_connector.rest._referral import get_distribution_history
    from orderly_evm_connector.rest._referral import check_ref_code
    from orderly_evm_connector.rest._referral import verify_ref_code
    from orderly_evm_connector.rest._referral import get_referral_rebate_summary
    from orderly_evm_connector.rest._referral import get_referral_info
    from orderly_evm_connector.rest._referral import get_referee_info
    from orderly_evm_connector.rest._referral import get_referee_history
    from orderly_evm_connector.rest._referral import edit_referral_split
    from orderly_evm_connector.rest._referral import create_referral_code
    from orderly_evm_connector.rest._referral import update_referral_code

    # rewards
    from orderly_evm_connector.rest._rewards import get_parameters_of_each_epoch
    from orderly_evm_connector.rest._rewards import get_broker_allocation_history
    from orderly_evm_connector.rest._rewards import get_account_trading_rewards_history
    from orderly_evm_connector.rest._rewards import get_wallet_trading_rewards_history
    from orderly_evm_connector.rest._rewards import get_epochs_data
    from orderly_evm_connector.rest._rewards import get_current_epoch_estimate
    from orderly_evm_connector.rest._rewards import get_current_epoch_estimate_broker
    from orderly_evm_connector.rest._rewards import get_parameters_of_each_mm_epoch
    from orderly_evm_connector.rest._rewards import get_wallet_group_mm_rewards_history
    from orderly_evm_connector.rest._rewards import get_market_maker_current_epoch_estimate
    from orderly_evm_connector.rest._rewards import get_wallet_staked_balance
    from orderly_evm_connector.rest._rewards import get_staking_overview
    from orderly_evm_connector.rest._rewards import get_unstake_details
    from orderly_evm_connector.rest._rewards import get_valor_batch_info
    from orderly_evm_connector.rest._rewards import get_valor_pool_info
    from orderly_evm_connector.rest._rewards import get_valor_redeem_info
    from orderly_evm_connector.rest._rewards import get_wallet_trading_rewards_history
