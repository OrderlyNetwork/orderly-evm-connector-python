from orderly_evm_connector.lib.utils import check_required_parameters


def get_account(self):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/account
    """
    _message = {"id": self.wss_id, "topic": "account", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_balance(self):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/balance
    """
    _message = {"id": self.wss_id, "topic": "balance", "event": "subscribe"}
    self.send_message_to_server(_message)

def get_execution_report(self):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-evm/evm-api/introduction#websocket-api-private-notifications
    """
    _message = {"id": self.wss_id, "topic": "executionreport", "event": "subscribe"}
    self.send_message_to_server(_message)

def get_execution_report_by_symbol(self, symbol):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-evm/evm-api/introduction#websocket-api-private-notifications
    """
    _message = {
        "id": self.wss_id,
        "topic": "executionreport",
        "event": "subscribe",
        "params": {"symbol": symbol}
        }
    self.send_message_to_server(_message)

def get_algo_execution_report(self):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/algo-execution-report
    """
    _message = {"id": self.wss_id, "topic": "algoexecutionreport", "event": "subscribe"}
    self.send_message_to_server(_message)

def get_algo_execution_report_v2(self):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/algo-execution-report-v2
    """
    _message = {"id": self.wss_id, "topic": "algoexecutionreportv2", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_notifications(self):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/notifications
    """
    _message = {"id": self.wss_id, "topic": "notifications", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_position(self):
    """
    Push interval: push on update
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/position-push
    """
    _message = {"id": self.wss_id, "topic": "position", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_account_liquidations(self):
    """Push interval: push on update
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/liquidation-account-push
    """
    _message = {"id": self.wss_id, "topic": "liquidationsaccount", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_liquidator_liquidations(self):
    """
    Push interval: push on addition/removal/update from list within 1s
    1 user_id can have many liquidation_ids
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/liquidator
    """
    _message = {
        "id": self.wss_id,
        "topic": "liquidatorliquidations",
        "event": "subscribe",
    }
    self.send_message_to_server(_message)


def get_pnl_settlement(self):
    """
    Push interval: real-time push on update
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/pnl-settlement
    """
    _message = {"id": self.wss_id, "topic": "settle", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_wallet_transactions(self):
    """
    Push interval: real-time push
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/wallet-transactions
    """
    _message = {"id": self.wss_id, "topic": "wallet", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_asset_convert(self):
    """
    Push interval: push on update
    https://orderly.network/docs/build-on-omnichain/evm-api/websocket-api/private/asset-convert
    """
    _message = {"id": self.wss_id, "topic": "assetconvert", "event": "subscribe"}
    self.send_message_to_server(_message)