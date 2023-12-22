# from orderly_evm_connector.websocket.websocket_api import WebsocketAPIClient as WebsocketClients
from utils.config import get_account_info
import time, logging
from orderly_evm_connector.websocket.websocket_api import WebsocketPublicAPIClient

(
    orderly_key,
    orderly_secret,
    orderly_account_id,
    wallet_secret,
    orderly_testnet,
    wss_id,
) = get_account_info()


def on_close(_):
    logging.info("Do custom stuff when connection is closed")


def message_handler(_, message):
    logging.info(message)


# Public websocket does not need to pass orderly_key and orderly_secret arguments

wss_client = WebsocketPublicAPIClient(
    orderly_testnet=orderly_testnet,
    orderly_account_id=orderly_account_id,
    wss_id=wss_id,
    on_message=message_handler,
    on_close=on_close,
    debug=True,
)

# #Request orderbook data
# wss_client.request_orderbook('orderbook','PERP_BTC_USDC')
# #orderbook depth 100 push every 1s
# wss_client.get_orderbook('PERP_NEAR_USDC@orderbook')
# #orderbookupdate updated orderbook push every 200ms
# wss_client.get_orderbookupdate('PERP_NEAR_USDC@orderbookupdate')
# wss_client.get_trade('PERP_NEAR_USDC@trade')
# wss_client.get_24h_ticker('PERP_NEAR_USDC@ticker')
wss_client.get_24h_tickers()
# wss_client.get_bbo('PERP_NEAR_USDC@bbo')
# wss_client.get_bbos()
# wss_client.get_kline("PERP_NEAR_USDC@kline_1m")
# wss_client.get_index_price('PERP_ETH_USDC@indexprice')
# wss_client.get_index_prices()
# wss_client.get_mark_price('PERP_ETH_USDC@markprice')
# wss_client.get_mark_prices()
# wss_client.get_open_interest('PERP_ETH_USDC@openinterest')
# wss_client.get_estimated_funding_rate('PERP_BTC_USDC@estfundingrate')
# wss_client.get_liquidation_push()

time.sleep(1000)
wss_client.stop()
