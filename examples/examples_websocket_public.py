# from orderly_evm_connector.websocket.websocket_api import WebsocketAPIClient as WebsocketClients
import asyncio
import logging
import os
import time

from asgiref.sync import sync_to_async

from orderly_evm_connector.websocket.websocket_api import (
    WebsocketPublicAPIClient,
    WebsocketPublicAPIClientAsync,
)
from utils.config import get_account_info

logging.basicConfig(level=logging.INFO)

LISTEN_SECONDS = int(os.getenv("ORDERLY_PUBLIC_WS_LISTEN_SECONDS", "60"))


def on_close(_):
    logging.info("Do custom stuff when connection is closed")


def message_handler(_, message):
    logging.info(message)


async def request_orderbook(client_async):
    await client_async.run()
    await client_async.request_orderbook("orderbook", "PERP_BTC_USDC")
    await asyncio.sleep(100)


def main():
    (
        orderly_key,
        orderly_secret,
        orderly_account_id,
        wallet_secret,
        orderly_testnet,
        wss_id,
    ) = get_account_info()

    # Public websocket does not need to pass orderly_key and orderly_secret arguments
    wss_client = WebsocketPublicAPIClient(
        orderly_testnet=orderly_testnet,
        orderly_account_id=orderly_account_id,
        wss_id=wss_id,
        on_message=message_handler,
        on_close=on_close,
        debug=True,
    )

    try:
        # # Request orderbook data
        # wss_client.request_orderbook('orderbook','PERP_BTC_USDC')
        # # orderbook depth 100 push every 1s
        # wss_client.get_orderbook('PERP_ETH_USDC@orderbook')
        # wss_client.get_orderbook('PERP_NEAR_USDC@orderbook')
        # # orderbookupdate updated orderbook push every 200ms
        # wss_client.get_orderbookupdate('PERP_ETH_USDC@orderbookupdate')
        # wss_client.get_trade('PERP_BTC_USDC@trade')
        # wss_client.get_24h_ticker('PERP_BTC_USDC@ticker')
        # wss_client.get_24h_tickers()
        # wss_client.get_24h_ticker_by_builder("woofi_pro", "PERP_BTC_USDC")
        # wss_client.get_24h_tickers_by_builder("woofi_pro")
        # wss_client.get_bbo('PERP_BTC_USDC@bbo')
        # wss_client.get_bbos()
        # wss_client.get_kline("PERP_BTC_USDC@kline_1m")
        # wss_client.get_market_price_changes_info()
        # wss_client.get_traders_open_interest()
        # wss_client.get_price_for_small_charts("1h")
        # wss_client.get_index_price('SPOT_ETH_USDC@indexprice')
        # wss_client.get_index_prices()
        # wss_client.get_mark_price('PERP_ETH_USDC@markprice')
        # wss_client.get_mark_prices()
        # wss_client.get_open_interest('PERP_ETH_USDC@openinterest')
        # wss_client.get_estimated_funding_rate('PERP_BTC_USDC@estfundingrate')
        wss_client.get_liquidation_push()
        # wss_client.get_system_maintenance_status()
        # wss_client.get_announcement()

        logging.info(
            "Listening for public websocket messages for %s seconds...",
            LISTEN_SECONDS,
        )
        time.sleep(LISTEN_SECONDS)
    finally:
        logging.info("closing public ws connection")
        wss_client.stop()


if __name__ == "__main__":
    main()
