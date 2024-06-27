from orderly_evm_connector.lib.utils import check_required_parameters


def get_account(self):
    """Push interval: real-time push
    https://docs-api-evm.orderly.network/#websocket-api-private-account
    """
    _message = {"id": self.wss_id, "topic": "account", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_balance(self):
    """Push interval: real-time push
    https://docs-api-evm.orderly.network/#websocket-api-private-balance
    """
    _message = {"id": self.wss_id, "topic": "balance", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_position(self):
    """Push interval: push on update
    https://docs-api-evm.orderly.network/#websocket-api-private-position-push
    """
    _message = {"id": self.wss_id, "topic": "position", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_account_liquidations(self):
    """Push interval: push on update
    https://docs-api-evm.orderly.network/#websocket-api-private-account-liquidations
    """
    _message = {"id": self.wss_id, "topic": "liquidationsaccount", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_liquidator_liquidations(self):
    """Push interval: push on addition/removal/update from list within 1s
                      1 user_id can have many liquidation_ids
    https://docs-api-evm.orderly.network/#websocket-api-private-liquidator-liquidations
    """
    _message = {
        "id": self.wss_id,
        "topic": "liquidatorliquidations",
        "event": "subscribe",
    }
    self.send_message_to_server(_message)


def get_wallet_transactions(self):
    """Push interval: real-time push on update
    https://docs-api-evm.orderly.network/#websocket-api-private-wallet-transactions
    """
    _message = {"id": self.wss_id, "topic": "wallet", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_pnl_settlement(self):
    """Push interval: real-time push on update
    https://docs-api-evm.orderly.network/#websocket-api-private-pnl-settlement
    """
    _message = {"id": self.wss_id, "topic": "settle", "event": "subscribe"}
    self.send_message_to_server(_message)


def get_notifications(self):
    """Push interval: real-time push
    https://docs-api-evm.orderly.network/#websocket-api-private-notifications
    """
    _message = {"id": self.wss_id, "topic": "notifications", "event": "subscribe"}
    self.send_message_to_server(_message)

def get_execution_report(self):
    """Push interval: real-time push
    https://orderly.network/docs/build-on-evm/evm-api/introduction#websocket-api-private-notifications
    """
    _message = {"id": self.wss_id, "topic": "executionreport", "event": "subscribe"}
    self.send_message_to_server(_message)

def get_algo_execution_report(self):
    """Push interval: real-time push
    https://orderly.network/docs/build-on-evm/evm-api/introduction#websocket-api-private-notifications
    """
    _message = {"id": self.wss_id, "topic": "algoexecutionreportv2", "event": "subscribe"}
    self.send_message_to_server(_message)

def get_execution_report_for_single_broker(self, broker_id):
    """Push interval: real-time push
    https://orderly.network/docs/build-on-evm/evm-api/introduction#websocket-api-private-notifications
    """
    check_required_parameters([[broker_id, "broker_id"]])
    _message = {
        "id": self.wss_id,
        "topic": f"executionreport@{broker_id}",
        "event": "subscribe",
        "broker_id": broker_id,
    }
    self.send_message_to_server(_message)