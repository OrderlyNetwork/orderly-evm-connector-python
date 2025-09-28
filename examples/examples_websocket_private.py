import logging
import os
import time

from orderly_evm_connector.websocket.websocket_api import WebsocketPrivateAPIClient
from utils.config import get_account_info

logging.basicConfig(level=logging.INFO)

LISTEN_SECONDS = int(os.getenv("ORDERLY_PRIVATE_WS_LISTEN_SECONDS", "60"))


def on_close(_):
    logging.info("Do custom stuff when connection is closed")


def message_handler(_, message):
    logging.info(message)


def main():
    (
        orderly_key,
        orderly_secret,
        orderly_account_id,
        wallet_secret,
        orderly_testnet,
        wss_id,
    ) = get_account_info()

    wss_client = WebsocketPrivateAPIClient(
        orderly_testnet=orderly_testnet,
        orderly_account_id=orderly_account_id,
        wss_id=wss_id,
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
        on_message=message_handler,
        on_close=on_close,
        debug=True,
    )

    try:
        wss_client.get_account()
        # wss_client.get_balance()
        # wss_client.get_position()
        # wss_client.get_account_liquidations()
        # wss_client.get_liquidator_liquidations()
        # wss_client.get_wallet_transactions()
        # wss_client.get_pnl_settlement()
        # wss_client.get_notifications()
        # wss_client.get_execution_report()
        # wss_client.get_algo_execution_report()
        # wss_client.get_execution_report_for_single_broker(broker_id="woofi-pro")
        logging.info(
            "Listening for private websocket messages for %s seconds...",
            LISTEN_SECONDS,
        )
        time.sleep(LISTEN_SECONDS)
    finally:
        logging.info("closing ws connection")
        wss_client.stop()


if __name__ == "__main__":
    main()
