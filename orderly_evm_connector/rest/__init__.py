from orderly_evm_connector.api import API

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
    from orderly_evm_connector.rest._account import get_registration_nonce
    from orderly_evm_connector.rest._account import get_account
    from orderly_evm_connector.rest._account import register_account
    from orderly_evm_connector.rest._account import get_orderly_key
    from orderly_evm_connector.rest._account import add_orderly_key
    from orderly_evm_connector.rest._account import update_leverage_configuration
    from orderly_evm_connector.rest._account import get_current_holdings
    from orderly_evm_connector.rest._account import get_account_information
    from orderly_evm_connector.rest._account import set_maintenance_config
    from orderly_evm_connector.rest._account import get_user_daily_volume
    from orderly_evm_connector.rest._account import get_user_volume_statistics
    from orderly_evm_connector.rest._account import get_current_orderlykey_info
    from orderly_evm_connector.rest._account import get_orderlykey_ip_restriction
    from orderly_evm_connector.rest._account import set_orderlykey_ip_restriction
    from orderly_evm_connector.rest._account import reset_orderlykey_ip_restriction

    # broker
    from orderly_evm_connector.rest._broker import get_list_of_brokers

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

    # onchain
    from orderly_evm_connector.rest._onchain import get_valut_balances
    from orderly_evm_connector.rest._onchain import get_valut_chain_config

    # settlement
    from orderly_evm_connector.rest._settlement import get_settle_pnl_nonce
    from orderly_evm_connector.rest._settlement import request_pnl_settlement
    from orderly_evm_connector.rest._settlement import get_pnl_settlement_history

    # trade
    from orderly_evm_connector.rest._trade import create_order
    from orderly_evm_connector.rest._trade import batch_create_order
    from orderly_evm_connector.rest._trade import edit_order
    from orderly_evm_connector.rest._trade import cancel_order
    from orderly_evm_connector.rest._trade import cancel_order_by_client_order_id
    from orderly_evm_connector.rest._trade import cancel_orders
    from orderly_evm_connector.rest._trade import batch_cancel_orders
    from orderly_evm_connector.rest._trade import batch_cancel_orders_by_client_order_id
    from orderly_evm_connector.rest._trade import get_order
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
