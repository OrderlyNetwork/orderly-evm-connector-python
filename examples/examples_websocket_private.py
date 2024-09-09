from utils.config import get_account_info
import time, logging
from orderly_evm_connector.websocket.websocket_api import WebsocketPrivateAPIClient

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


wss_client = WebsocketPrivateAPIClient(
    orderly_testnet=orderly_testnet,
    orderly_account_id=orderly_account_id,
    wss_id=wss_id,
    orderly_key=orderly_key,
    orderly_secret=orderly_secret,
    on_message=message_handler,
    on_close=on_close,
)

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
#wss_client.get_execution_report_for_single_broker(broker_id="woofi-pro")
# time.sleep(10000)

logging.info("closing ws connection")
wss_client.stop()
