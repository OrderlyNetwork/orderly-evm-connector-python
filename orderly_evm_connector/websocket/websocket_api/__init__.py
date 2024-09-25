import asyncio
from typing import Optional
from orderly_evm_connector.websocket.websocket_client import OrderlyWebsocketClient
from orderly_evm_connector.lib.utils import get_endpoints


class WebsocketPublicAPIClient(OrderlyWebsocketClient):
    def __init__(
        self,
        orderly_testnet=False,
        orderly_account_id=None,
        orderly_key=None,
        orderly_secret=None,
        private=False,
        wss_id=None,
        timeout=None,
        debug=False,
        proxies: Optional[dict] = None,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
    ):
        _, self.orderly_websocket_public_endpoint, _ = get_endpoints(orderly_testnet)
        super().__init__(
            self.orderly_websocket_public_endpoint,
            wss_id=wss_id,
            private=private,
            orderly_account_id=orderly_account_id,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            timeout=timeout,
            debug=debug,
            proxies=proxies,
        )

    from orderly_evm_connector.websocket.websocket_api._stream import get_orderbook
    from orderly_evm_connector.websocket.websocket_api._stream import request_orderbook
    from orderly_evm_connector.websocket.websocket_api._stream import (
        get_orderbookupdate,
    )
    from orderly_evm_connector.websocket.websocket_api._stream import get_trade
    from orderly_evm_connector.websocket.websocket_api._stream import get_24h_ticker
    from orderly_evm_connector.websocket.websocket_api._stream import get_24h_tickers
    from orderly_evm_connector.websocket.websocket_api._stream import get_bbo
    from orderly_evm_connector.websocket.websocket_api._stream import get_bbos
    from orderly_evm_connector.websocket.websocket_api._stream import get_kline
    from orderly_evm_connector.websocket.websocket_api._stream import get_index_price
    from orderly_evm_connector.websocket.websocket_api._stream import get_index_prices
    from orderly_evm_connector.websocket.websocket_api._stream import get_mark_price
    from orderly_evm_connector.websocket.websocket_api._stream import get_mark_prices
    from orderly_evm_connector.websocket.websocket_api._stream import get_open_interest
    from orderly_evm_connector.websocket.websocket_api._stream import (
        get_estimated_funding_rate,
    )
    from orderly_evm_connector.websocket.websocket_api._stream import (
        get_liquidation_push,
    )

class WebsocketPublicAPIClientAsync(OrderlyWebsocketClient):
    def __init__(
        self,
        orderly_testnet=False,
        orderly_account_id=None,
        orderly_key=None,
        orderly_secret=None,
        private=False,
        wss_id=None,
        timeout=None,
        debug=False,
        proxies: Optional[dict] = None,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
    ):
        _, self.orderly_websocket_public_endpoint, _ = get_endpoints(orderly_testnet)
        super().__init__(
            self.orderly_websocket_public_endpoint,
            wss_id=wss_id,
            private=private,
            async_mode=True,
            orderly_account_id=orderly_account_id,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            timeout=timeout,
            debug=debug,
            proxies=proxies,
        )

    # public websocket
    async def request_orderbook(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import request_orderbook
        request_orderbook(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_orderbookupdate(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import (
            get_orderbookupdate,
        )
        get_orderbookupdate(self, *args, **kwargs)
        await asyncio.sleep(0)
    
    async def get_orderbook(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_orderbook
        get_orderbook(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_trade(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_trade
        get_trade(self, *args, **kwargs)
        await asyncio.sleep(0)
    
    async def get_24h_ticker(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_24h_ticker
        get_24h_ticker(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_24h_tickers(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_24h_tickers
        get_24h_tickers(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_bbo(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_bbo
        get_bbo(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_bbos(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_bbos
        get_bbos(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_kline(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_kline
        get_kline(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_index_price(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_index_price
        get_index_price(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_index_prices(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_index_prices
        get_index_prices(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_mark_price(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_mark_price
        get_mark_price(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_mark_prices(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_mark_prices
        get_mark_prices(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_open_interest(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import get_open_interest
        get_open_interest(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_estimated_funding_rate(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import (
            get_estimated_funding_rate,
        )
        get_estimated_funding_rate(self, *args, **kwargs)
        await asyncio.sleep(0)

    async def get_liquidation_push(self, *args, **kwargs):
        from orderly_evm_connector.websocket.websocket_api._stream import (
            get_liquidation_push,
        )
        get_liquidation_push(self, *args, **kwargs)
        await asyncio.sleep(0)


class WebsocketPrivateAPIClient(OrderlyWebsocketClient):
    def __init__(
        self,
        orderly_testnet=False,
        orderly_account_id=None,
        orderly_key=None,
        orderly_secret=None,
        private=True,
        wss_id=None,
        timeout=None,
        debug=False,
        proxies: Optional[dict] = None,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
    ):
        _, _, self.orderly_websocket_private_endpoint = get_endpoints(orderly_testnet)
        super().__init__(
            self.orderly_websocket_private_endpoint,
            orderly_account_id=orderly_account_id,
            orderly_key=orderly_key,
            orderly_secret=orderly_secret,
            private=private,
            wss_id=wss_id,
            timeout=timeout,
            debug=debug,
            proxies=proxies,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
        )

    # private websocket
    from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_account,
    )

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_balance,
    )
  

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_position,
    )
 

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_account_liquidations,
    )

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_liquidator_liquidations,
    )

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_wallet_transactions,
    )

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
            get_pnl_settlement,
    )

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
            get_notifications,
    )

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
            get_execution_report,
    )

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
            get_algo_execution_report,
    )

    from orderly_evm_connector.websocket.websocket_api._private_stream import (
            get_execution_report_for_single_broker,
    )

class WebsocketPrivateAPIClientAsync(OrderlyWebsocketClient):
  def __init__(
        self,
        orderly_testnet=False,
        orderly_account_id=None,
        orderly_key=None,
        orderly_secret=None,
        private=True,
        wss_id=None,
        timeout=None,
        debug=False,
        proxies: Optional[dict] = None,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
    ):
        _, _, self.orderly_websocket_private_endpoint = get_endpoints(orderly_testnet)
        super().__init__(
            self.orderly_websocket_private_endpoint,
            orderly_account_id=orderly_account_id,
            orderly_key=orderly_key,
            orderly_secret=orderly_secret,
            private=private,
            wss_id=wss_id,
            timeout=timeout,
            async_mode=True,
            debug=debug,
            proxies=proxies,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
        )
        
    # private websocket
  from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_account,
  )
  from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_balance,
  )
  from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_position,
  )
  from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_account_liquidations,
  )
  from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_liquidator_liquidations,
  )
  from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_wallet_transactions,
  )
  from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_pnl_settlement,
  )
  from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_notifications,
  )
  from orderly_evm_connector.websocket.websocket_api._private_stream import (
        get_execution_report,
        get_algo_execution_report,
        get_execution_report_for_single_broker
  )
