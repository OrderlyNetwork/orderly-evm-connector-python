import asyncio
import logging
import os

from orderly_evm_connector.websocket.websocket_api import WebsocketPrivateAPIClientAsync
from utils.config import get_account_info

logging.basicConfig(level=logging.INFO)

LISTEN_SECONDS = int(os.getenv("ORDERLY_PRIVATE_WS_ASYNC_LISTEN_SECONDS", "60"))


async def on_close(_):
    logging.info("Do custom stuff when async connection is closed")


async def message_handler(_, message):
    logging.info(message)


async def main():
    (
        orderly_key,
        orderly_secret,
        orderly_account_id,
        _wallet_secret,
        orderly_testnet,
        wss_id,
    ) = get_account_info()

    wss_client = WebsocketPrivateAPIClientAsync(
        orderly_testnet=orderly_testnet,
        orderly_account_id=orderly_account_id,
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
        wss_id=wss_id,
        on_message=message_handler,
        on_close=on_close,
        debug=True,
    )

    await wss_client.run()
    wss_client.get_account()
    logging.info(
        "Listening for async private websocket messages for %s seconds...",
        LISTEN_SECONDS,
    )
    await asyncio.sleep(LISTEN_SECONDS)
    await wss_client.stop_async()


if __name__ == "__main__":
    asyncio.run(main())
