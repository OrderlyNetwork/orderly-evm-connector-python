from orderly_evm_connector.rest import Rest as Client
from utils.config import get_account_info
from orderly_evm_connector.error import ClientError
import logging

(
    orderly_key,
    orderly_secret,
    orderly_account_id,
    wallet_secret,
    orderly_testnet,
    wss_id,
) = get_account_info()

client_public = Client(wallet_secret=wallet_secret, orderly_testnet=orderly_testnet,debug=True)

client_private = Client(
    orderly_key=orderly_key,
    orderly_secret=orderly_secret,
    orderly_account_id=orderly_account_id,
    wallet_secret=wallet_secret,
    orderly_testnet=orderly_testnet,
    debug=True
)

# #account
# #Check whether a particular account is registered on Orderly Network
# #You can catch exceptions in the following ways
# try:
#     response = client_public.get_account(
#         "0x036Cb579025d3535a0ADcD929D05481a3189714b", "woofi_pro"
#     )
#     logging.info(response)
# except ClientError as error:
#     logging.error(
#         "Found error. status: {}, error code: {}, error message: {}".format(
#             error.status_code, error.error_code, error.error_message
#         )
#     )
# #Get Account Details
# client_public.get_account_details("0x036Cb579025d3535a0ADcD929D05481a3189714b")
# #Get Registration Nonce
# client_public.get_registration_nonce()
# #Register Account
# client_public.register_account("woofi_pro",80001,190002888515,"xxxx")
# #Get Orderly Key
# client_public.get_orderly_key("0xaaa","ed25519:xxx")
# # #Add Orderly Key
# client_public.add_orderly_key(
#     "woofi_pro",
#     80001,
#     "ed25519:3mqrwZS7D4A7jktS7wg2yKUQJJJXYNYNtqem1zHFgykJ",
#     "read,trading",
#     1701316677000,
#     1703908677000,
#     "xxxx",
# )
# #Update leverage setting
# client_private.update_leverage_configuration(1)
# #Get the current summary of user token holdings.
# client_private.get_current_holdings(True)
# #Get basic account information including current user fee rates
# client_private.get_account_information()
# #Set the user config for whether the system should automatically cancel the user's pending orders during maintenance.
# client_private.set_maintenance_config(True)
# #Get User Daily Statistics
# client_private.get_user_daily_statistics(start_date="2023-01-01",end_date="2024-01-02")
# #Get the daily historical breakdown of the user trading volume.
# client_private.get_user_daily_volume(start_date="2023-01-01",end_date="2023-01-02")
# #Get the latest volume statistics of the user.
# client_private.get_user_volume_statistics()
# #Get current Orderly key info
# client_private.get_current_orderlykey_info()
# # ip restriction
# #Get Orderly Key IP restriction
# client_private.get_orderlykey_ip_restriction("ed25519:xxx")
# #Set Orderly key IP restriction
# client_private.set_orderlykey_ip_restriction("ed25519:xxx","1.1.1.1,2.2.2.2")
# #Reset orderly key IP restriction
# client_private.reset_orderlykey_ip_restriction("ed25519:xxx","ALLOW_ALL_IPS")

# #Broker
# #Get list of brokers
# client_public.get_list_of_brokers()
# #Get the user fee rate information
# client_private.get_user_fee_tier(account_id="0xdd26e7ec6f9aef279f5988ab0c71c6c8f0845b811d1ccca3d6944846d683460d")
# #Get Broker Daily Volume
# client_private.get_broker_daily_volume(start_date="2023-12-01",end_date="2024-02-02")
# #general
# #System maintenance status
# client_public.get_system_maintenance_status()
# #Get vault chain config
# client_public.get_faucet_usdc("43113","0x036Cb579025d3535a0ADcD929D05481a3189714b")
# #Available symbols
# client_public.get_exchange_info("PERP_ETH_USDC")
# #Token info
# client_public.get_token_info()
# #Available symbols
# client_public.get_available_symbols()
# #Futures fee information
# client_public.get_fee_futures_information()
# #Get leverage configuration
# client_public.get_leverage_configuration()
# #Get statistics of the user account
# client_private.get_user_statistics()


# # liquidation
# #Get positions under liquidation
# client_public.get_positions_under_liquidation()
# #Get liquidated positions info
# client_public.get_liquidated_positions_info("PERP_ETH_USDC")
# #Get liquidated positions by Liquidator
# client_private.get_liquidated_positions_by_liquidator("PERP_ETH_USDC")
# #Get insurance fund info
# client_public.get_insurance_fund_info()
# #Get liquidated positions of account
# client_private.get_liquidated_positions_of_account()
# #Claim liquidated positions
# client_private.claim_liquidated_positions(1000,1.0)
# #Claim from insurance fund
# client_private.claim_from_insurance_fund(1000,"PERP_ETH_USDC",1.0)

# #market
# #Market trades
# client_public.get_market_trades("PERP_ETH_USDC")
# #Volume statistics
# client_public.get_volume_statistics()
# #Get predicted funding rate for all markets
# client_public.get_predicted_funding_rate_for_all_markets()
# #Get predicted funding rate for one market
# client_public.get_predicted_funding_rate_for_one_market("PERP_ETH_USDC")
# #Get funding rate history for one market
# client_public.get_funding_rate_history_for_one_market("PERP_ETH_USDC")
# # Get futures info for all markets
# client_public.get_futures_info_for_all_markets()
# #Get futures for one market
# client_public.get_futures_info_for_one_market("PERP_ETH_USDC")
# #Get TradingView localized configuration info
# client_public.get_tradingview_configuration("en")
# #Get TradingView history bars
# client_public.get_tradingview_history_basrs("PERP_ETH_USDC","D")
# #Get TradingView symbol info
# client_public.get_tradingview_symbol_info("MSFT")
# #Orderbook snapshot
# client_private.get_orderbook_snapshot("PERP_NEAR_USDC")
# #Get kline
# client_private.get_kline("PERP_ETH_USDC","5m")


# #notifications
# #Get all notifications
# client_private.get_all_notifications()
# #Get unread notification information
# client_private.get_unread_notifications()
# #Set read status of notifications
# client_private.set_read_status_notifications(1,[2140])
# #Set read status of all notifications
# client_private.set_read_status_all_notifications(1)


# #onchain
# #Get Vault Balances
# client_public.get_valut_balances()
# #Get vault chain config
# client_public.get_valut_chain_config()


# #settlement
# #Get Settle PnL nonce
# client_private.get_settle_pnl_nonce()
# # #Request PnL Settlement
# client_private.request_pnl_settlement("woofi_pro",421613,1,"0x5aaa")
# #Get PnL settlement history
# client_private.get_pnl_settlement_history()


# #wallet
# #Get asset history, including token deposits/withdrawals.
# client_private.get_asset_history()
# #Get Withdrawal Nonce
# client_private.get_withdraw_nonce()
# #Create Withdraw Request
# client_private.withdraw_request("woofi_pro",421613,"0x5aaa","USDC",100000000,3,"0x5aaa")


# #trade
# #Get one position info
# client_private.get_one_position_info("PERP_ETH_USDC")
# #Get all position info
# client_private.get_all_positions_info()
# #Get funding fee history
# client_private.get_funding_fee_history("PERP_ETH_USDC")
# #create order
# client_private.create_order("PERP_NEAR_USDC","LIMIT","BUY",order_price=1.8,order_quantity=100)
# #create algo order
# client_private.create_algo_order("STOP",100,"BUY","PERP_APT_USDC","MARKET",5.11)

    
# #Batch create order
# orders = [
#     {
#         "order_price": 1.8,
#         "order_quantity": 100,
#         "order_type": "LIMIT",
#         "side": "BUY",
#         "symbol": "PERP_NEAR_USDC",
#     },
#     {
#         "order_price": 1.9,
#         "order_quantity": 100,
#         "order_type": "LIMIT",
#         "side": "BUY",
#         "symbol": "PERP_NEAR_USDC",
#     },
# ]
# client_private.batch_create_order(orders)
# #Edit order
# client_private.edit_order("97417030","PERP_NEAR_USDC","LIMIT","BUY",order_price=1.88,order_quantity=100)
# #Edit algo order
# client_private.edit_algo_order("1000065",quantity=100,trigger_price=3.4)
#Cancel algo order
# client_private.cancel_algo_order("1000067","PERP_APT_USDC")
## Cancel algo all pending order
# client_private.cancel_algo_all_pending_order("PERP_APT_USDC")
# #Cancel order
# client_private.cancel_order("3268388","PERP_APT_USDC")
# #Cancel algo order by client_order_id
# client_private.cancel_algo_order_by_client_order_id(100090,"PERP_APT_USDC")
# #Cancel order by client_order_id
# client_private.cancel_order_by_client_order_id(100090,"PERP_NEAR_USDC")
# #Cancel a list of orders, filtered by symbol optionally
# client_private.cancel_orders("PERP_NEAR_USDC")
# #Batch cancel orders
# client_private.batch_cancel_orders("97417075,97417074")
# #Batch cancel orders by client_order_id
# client_private.batch_cancel_orders_by_client_order_id("111,112")
# #Get algo order information
# client_private.get_algo_order("1000070")
# #Get algo orders information
# client_private.get_algo_orders("STOP")
# #Get order information
# client_private.get_order("97417075")
# #Get algo order by client_order_id
# client_private.get_algo_order_by_client_order_id("100090")
# #Get order by client_order_id
# client_private.get_order_by_client_order_id("100090")
# #Get orders by customized filters
# client_private.get_orders(symbol="PERP_NEAR_USDC")
# #Get all trades of a specific order
# client_private.get_all_trades_of_order("97417073")
# #Get client’s trades history within a time range
# client_private.get_trades("PERP_NEAR_USDC")
# #Get specific transaction details by trade_id
# client_private.get_trade("21570")

# #campaign
# #Get Number of Points for Distribution
# client_public.get_points_epoch()
