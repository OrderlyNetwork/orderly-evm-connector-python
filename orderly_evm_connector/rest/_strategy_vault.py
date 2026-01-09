from typing import Optional
from orderly_evm_connector.lib.enums import SVPayloadType
from orderly_evm_connector.lib.utils import check_required_parameters, generate_signature

def get_strategy_vault_nonce(self):
    """
    Get Strategy Vault Nonce for Account Transaction
    
    GET /v1/public/sv_nonce
    
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-nonce-for-account-transaction
    """
    return self._request("GET", "/v1/public/sv_nonce")


def submit_sv_operation_request(
        self,
        payload_type: int,
        nonce: str,
        receiver: str,
        amount: str,
        vault_id: str,
        token: str,
        dex_broker_id: str,
        chain_id: int,
        chain_type: str,
        signature: str,
        user_address: str,
        verifying_contract: str
):
    """
    Create Strategy Vault Deposit/Withdrawal Request with Account

    POST /v1/sv_operation_request

    Args:
        payload_type(int): Type of operation (LP_DEPOSIT=0, LP_WITHDRAW=1, SP_DEPOSIT=2, SP_WITHDRAW=3)
        nonce(str): Unique nonce string
        receiver(str): Receiver address
        amount(str): Amount to deposit/withdraw
        vault_id(str): Vault ID
        token(str): Token symbol
        dex_broker_id(str): DEX broker ID
        chain_id(int): Chain ID
        chain_type(str): Chain type
        signature(str): Signature for the message
        user_address(str): User's address
        verifying_contract(str): Verifying contract address

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/submit-sv-operation-request
    """
    # Validate required parameters
    check_required_parameters([
        [payload_type, "payload_type"],
        [nonce, "nonce"],
        [receiver, "receiver"],
        [amount, "amount"],
        [vault_id, "vault_id"],
        [token, "token"],
        [dex_broker_id, "dex_broker_id"],
        [chain_id, "chain_id"],
        [chain_type, "chain_type"],
        [signature, "signature"],
        [user_address, "user_address"],
        [verifying_contract, "verifying_contract"]
    ])

    # Construct message body
    message = {
        "payloadType": payload_type,
        "nonce": nonce,
        "receiver": receiver,
        "amount": amount,
        "vaultId": vault_id,
        "token": token,
        "dexBrokerId": dex_broker_id,
        "chainId": chain_id,
        "chainType": chain_type
    }

    payload = {
        "message": message,
        "signature": signature,
        "userAddress": user_address,
        "verifyingContract": verifying_contract
    }
    return self._sign_request("POST", "/v1/sv_operation_request", payload=payload)


def get_account_strategy_vault_transaction_history(
    self, 
    vault_id: Optional[str] = None, 
    type: Optional[str] = None, 
    status: Optional[str] = None,
    start_t: Optional[int] = None,
    end_t: Optional[int] = None,
    page: Optional[int] = None,
    size: Optional[int] = None
):
    """
    Get Account's Strategy Vault Transaction History
    
    GET /v1/account_sv_transaction_history
    
    Optional Args:
        vault_id(str): Vault ID
        type(str): Transaction type (deposit/withdrawal)
        status(str): Transaction status (pending/processing/completed/failed)
        start_t(int): Start time in milliseconds
        end_t(int): End time in milliseconds
        page(int): Page number (default: 1)
        size(int): Number of records per page (default: 25)
    
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/account_sv_transaction_history
    """
    payload = {
        "vault_id": vault_id,
        "type": type,
        "status": status,
        "start_t": start_t,
        "end_t": end_t,
        "page": page,
        "size": size
    }
    return self._sign_request("GET", "/v1/account_sv_transaction_history", payload=payload)


def add_sp_orderly_key(
    self,
    brokerId: str,
    chainId: int,
    orderlyKey: str,
    scope: str,
    timestamp: int,
    expiration: int,
    userAddress: str,
    subAccountId: str,
    contract: str = None,
    **kwargs
):
    """Add SP Orderly Key
    
    Limit: 10 requests per second per IP address
    
    POST /v1/sv/sp_orderly_key
    
    Adds an Orderly access key to a SP account
    
    Args:
        brokerId(string): Broker ID
        chainId(int): Chain ID
        orderlyKey(string): The public key of the Orderly access key
        scope(string): Scope of the key
        timestamp(int): Timestamp in UNIX milliseconds
        expiration(int): Expiration timestamp
        userAddress(string): User address
        subAccountId(string): Create the api key for the input subAccountId
        
    Optional Args:
        contract(string): Contract address
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/add-sp-orderly-key
    """
    from orderly_evm_connector.lib.utils import check_required_parameters, get_timestamp
    check_required_parameters([
        [brokerId, "brokerId"],
        [chainId, "chainId"],
        [orderlyKey, "orderlyKey"],
        [scope, "scope"],
        [expiration, "expiration"],
        [userAddress, "userAddress"],
        [subAccountId, "subAccountId"]
    ])
    
    _message = {
        "brokerId": brokerId,
        "chainId": chainId,
        "orderlyKey": orderlyKey,
        "scope": scope,
        "timestamp": int(get_timestamp()) if not timestamp else timestamp,
        "expiration": expiration,
        "subAccountId": subAccountId
    }
    if contract:
        _message["contract"] = contract
    
    message = {
        "domain": {
            "name": "Orderly",
            "version": "1",
            "chainId": chainId,
            "verifyingContract": contract or "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC",
        },
        "message": _message,
        "primaryType": "AddSPOrderlyKey",
        "types": {
            "EIP712Domain": [
                {"name": "name", "type": "string"},
                {"name": "version", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "verifyingContract", "type": "address"},
            ],
            "AddSPOrderlyKey": [
                {"name": "brokerId", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "orderlyKey", "type": "string"},
                {"name": "scope", "type": "string"},
                {"name": "timestamp", "type": "uint64"},
                {"name": "expiration", "type": "uint64"},
                {"name": "subAccountId", "type": "string"},
            ],
        },
    }
    if contract:
        message["types"]["AddSPOrderlyKey"].append({"name": "contract", "type": "string"})
    
    _signature = self.get_wallet_signature(message=message)
    payload = {
        "message": _message,
        "signature": _signature,
        "userAddress": userAddress,
        **kwargs
    }
    return self._sign_request("POST", "/v1/sv/sp_orderly_key", payload=payload)


def request_sp_settle_pnl(
    self,
    brokerId: str,
    chainId: int,
    settleNonce: str,
    userAddress: str,
    verifyingContract: str,
    contract: str = None,
    timestamp: int = None,
    **kwargs
):
    """Request SP PnL Settlement
    
    Limit: 1 request per second
    
    POST /v1/sv/sp_settle_pnl
    
    Args:
        brokerId(string): Broker ID
        chainId(int): Chain ID
        settleNonce(string): Settlement nonce
        userAddress(string): User address
        verifyingContract(string): Verifying contract address
        
    Optional Args:
        contract(string): Contract address
        timestamp(int): Timestamp in UNIX milliseconds
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/request-sp-pnl-settlement
    """
    from orderly_evm_connector.lib.utils import check_required_parameters, get_timestamp
    check_required_parameters([
        [brokerId, "brokerId"],
        [chainId, "chainId"],
        [settleNonce, "settleNonce"],
        [userAddress, "userAddress"],
        [verifyingContract, "verifyingContract"]
    ])
    
    _message = {
        "brokerId": brokerId,
        "chainId": chainId,
        "settleNonce": settleNonce,
        "timestamp": int(get_timestamp()) if not timestamp else timestamp,
    }
    if contract:
        _message["contract"] = contract
    
    message = {
        "domain": {
            "name": "Orderly",
            "version": "1",
            "chainId": chainId,
            "verifyingContract": verifyingContract,
        },
        "message": _message,
        "primaryType": "SettleSPPnl",
        "types": {
            "EIP712Domain": [
                {"name": "name", "type": "string"},
                {"name": "version", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "verifyingContract", "type": "address"},
            ],
            "SettleSPPnl": [
                {"name": "brokerId", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "settleNonce", "type": "string"},
                {"name": "timestamp", "type": "uint64"},
            ],
        },
    }
    if contract:
        message["types"]["SettleSPPnl"].append({"name": "contract", "type": "string"})
    
    _signature = self.get_wallet_signature(message=message)
    payload = {
        "message": _message,
        "signature": _signature,
        "userAddress": userAddress,
        "verifyingContract": verifyingContract,
        **kwargs
    }
    return self._sign_request("POST", "/v1/sv/sp_settle_pnl", payload=payload)


def trigger_manual_period_delivery(self, account_id: str, orderly_key: str, plan_id: str):
    """Trigger Manual Period Delivery
    
    Limit: 1 request per second per account
    
    POST /v1/sv/manual_period_delivery
    
    Args:
        account_id(string): Account ID
        orderly_key(string): Orderly key
        plan_id(string): Plan ID
        
    Note: This endpoint requires special authentication with account_id, orderly_key, and orderly_signature in query parameters.
    The signature should be generated for the request.
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/trigger-manual-period-delivery
    """
    import json
    check_required_parameters([
        [account_id, "account_id"],
        [orderly_key, "orderly_key"],
        [plan_id, "plan_id"]
    ])
    
    payload = {"plan_id": plan_id}
    # Build URL with query parameters
    url_path = f"/v1/sv/manual_period_delivery?account_id={account_id}&orderly_key={orderly_key}"
    
    # Prepare params for signature generation
    _payload = json.dumps(payload) if payload else ""
    query_string = f"POST{url_path}{_payload}"
    
    try:
        _timestamp, _signature = generate_signature(
            self.orderly_secret, message=query_string
        )
    except ValueError:
        _timestamp, _signature = "mock_timestamp", "mock_signature"
    
    # Add signature to URL
    url_path += f"&orderly_signature={_signature}"
    
    # Update headers
    self.session.headers.update({
        "orderly-timestamp": _timestamp,
        "orderly-account-id": account_id,
        "orderly-key": orderly_key,
        "orderly-signature": _signature,
    })
    
    return self.send_request("POST", url_path, payload=payload)


def get_venue_transfer_history(self, period_number: int = None, page: int = None, size: int = None):
    """Get Fund Inflow Allocation
    
    Limit: 10 requests per second per IP address
    
    GET /v1/sv/venue_transfer_history
    
    Optional Args:
        period_number(int): Period number
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-fund-inflow-allocation
    """
    payload = {
        "period_number": period_number,
        "page": page,
        "size": size
    }
    return self._sign_request("GET", "/v1/sv/venue_transfer_history", payload=payload)


def get_venue_withdrawal_history(self, period_number: int = None, page: int = None, size: int = None):
    """Get Fund Outflow Allocation
    
    Limit: 10 requests per second per account
    
    GET /v1/sv/venue_withdrawal_history
    
    Optional Args:
        period_number(int): Period number
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-fund-outflow-allocation
    """
    payload = {
        "period_number": period_number,
        "page": page,
        "size": size
    }
    return self._sign_request("GET", "/v1/sv/venue_withdrawal_history", payload=payload)


def get_protocol_revenue_share_history(self, page: int = None, size: int = None):
    """Get Orderly Protocol Revenue Sharing History
    
    Limit: 10 requests per second per account
    
    GET /v1/sv/protocol_revenue_share_history
    
    Optional Args:
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-orderly-protocol-revenue-sharing-history
    """
    payload = {
        "page": page,
        "size": size
    }
    return self._sign_request("GET", "/v1/sv/protocol_revenue_share_history", payload=payload)


def get_liquidation_fees_share_history(self, page: int = None, size: int = None):
    """Get Liquidation Fees Sharing History
    
    Limit: 10 requests per second per account
    
    GET /v1/sv/liquidation_fees_share_history
    
    Optional Args:
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-liquidation-fees-sharing-history
    """
    payload = {
        "page": page,
        "size": size
    }
    return self._sign_request("GET", "/v1/sv/liquidation_fees_share_history", payload=payload)


def get_sv_internal_transfer_history(self, page: int = None, size: int = None):
    """Get Internal Transfer History
    
    Limit: 10 requests per second per account
    
    GET /v1/sv/internal_transfer_history
    
    Non-Vault Account to Strategy Provider Account
    
    Optional Args:
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-internal-transfer-history
    """
    payload = {
        "page": page,
        "size": size
    }
    return self._sign_request("GET", "/v1/sv/internal_transfer_history", payload=payload)


# Vault related APIs
def get_sv_vault_info(self, vault_id: Optional[str] = None):
    """Get Strategy Vault Info
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/vault/info
    
    Optional Args:
        vault_id(str): Vault ID
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-info
    """
    payload = {"vault_id": vault_id} if vault_id else {}
    return self._request("GET", "/v1/public/strategy_vault/vault/info", payload=payload)


def get_sv_vault_overall_info(self):
    """Get Strategy Vault Overall Info
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/vault/overall_info
    
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-overall-info
    """
    return self._request("GET", "/v1/public/strategy_vault/vault/overall_info")


def get_sv_user_overall_info(self, address: Optional[str] = None):
    """Get Strategy Vault User Overall Info
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/user/overall_info
    
    Optional Args:
        address(str): User address
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-user-overall-info
    """
    payload = {"address": address} if address else {}
    return self._request("GET", "/v1/public/strategy_vault/user/overall_info", payload=payload)


def get_sv_vault_performance(self, vault_id: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
    """Get Strategy Vault Performance
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/vault/performance
    
    Optional Args:
        vault_id(str): Vault ID
        start_date(str): Start date (YYYY-MM-DD)
        end_date(str): End date (YYYY-MM-DD)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-performance
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if start_date:
        payload["start_date"] = start_date
    if end_date:
        payload["end_date"] = end_date
    return self._request("GET", "/v1/public/strategy_vault/vault/performance", payload=payload)


def get_sv_vault_performance_chart(self, vault_id: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
    """Get Strategy Vault Performance Chart
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/vault/performance_chart
    
    Optional Args:
        vault_id(str): Vault ID
        start_date(str): Start date (YYYY-MM-DD)
        end_date(str): End date (YYYY-MM-DD)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-performance-chart
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if start_date:
        payload["start_date"] = start_date
    if end_date:
        payload["end_date"] = end_date
    return self._request("GET", "/v1/public/strategy_vault/vault/performance_chart", payload=payload)


def get_sv_vault_positions(self, vault_id: Optional[str] = None):
    """Get Strategy Vault Positions
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/vault/positions
    
    Optional Args:
        vault_id(str): Vault ID
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-positions
    """
    payload = {"vault_id": vault_id} if vault_id else {}
    return self._request("GET", "/v1/public/strategy_vault/vault/positions", payload=payload)


def get_sv_vault_open_orders(self, vault_id: Optional[str] = None):
    """Get Strategy Vault Open Orders
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/vault/open_orders
    
    Optional Args:
        vault_id(str): Vault ID
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-open-orders
    """
    payload = {"vault_id": vault_id} if vault_id else {}
    return self._request("GET", "/v1/public/strategy_vault/vault/open_orders", payload=payload)


def get_sv_vault_trade_history(self, vault_id: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault Trade History
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/vault/trade_history
    
    Optional Args:
        vault_id(str): Vault ID
        page(int): Page number (start from 1)
        size(int): Page size (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-trade-history
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if page:
        payload["page"] = page
    if size:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/vault/trade_history", payload=payload)


def get_sv_vault_liquidator_history(self, vault_id: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault Liquidator History
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/vault/liquidator_history
    
    Optional Args:
        vault_id(str): Vault ID
        page(int): Page number (start from 1)
        size(int): Page size (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-liquidator-history
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if page:
        payload["page"] = page
    if size:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/vault/liquidator_history", payload=payload)


# LP related APIs
def get_sv_lp_info(self, vault_id: Optional[str] = None, address: Optional[str] = None):
    """Get Strategy Vault LP Info
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/lp/info
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-info
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    return self._request("GET", "/v1/public/strategy_vault/lp/info", payload=payload)


def get_sv_lp_performance(self, vault_id: Optional[str] = None, address: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
    """Get Strategy Vault LP Performance
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/lp/performance
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        start_date(str): Start date (YYYY-MM-DD)
        end_date(str): End date (YYYY-MM-DD)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-performance
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    if start_date:
        payload["start_date"] = start_date
    if end_date:
        payload["end_date"] = end_date
    return self._request("GET", "/v1/public/strategy_vault/lp/performance", payload=payload)


def get_sv_lp_performance_chart(self, vault_id: Optional[str] = None, address: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None):
    """Get Strategy Vault LP Performance Chart
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/lp/performance_chart
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        start_date(str): Start date (YYYY-MM-DD)
        end_date(str): End date (YYYY-MM-DD)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-performance-chart
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    if start_date:
        payload["start_date"] = start_date
    if end_date:
        payload["end_date"] = end_date
    return self._request("GET", "/v1/public/strategy_vault/lp/performance_chart", payload=payload)


def get_sv_lp_transaction_history(self, vault_id: Optional[str] = None, address: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault LP Transaction History
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/lp/transaction_history
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        page(int): Page number (start from 1)
        size(int): Page size (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-transaction-history
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    if page:
        payload["page"] = page
    if size:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/lp/transaction_history", payload=payload)


def get_sv_lp_claim_info(self, vault_id: Optional[str] = None, address: Optional[str] = None):
    """Get Strategy Vault LP Claim Info
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/lp/claim_info
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-claim-info
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    return self._request("GET", "/v1/public/strategy_vault/lp/claim_info", payload=payload)


def get_sv_lp_fees_history(self, vault_id: Optional[str] = None, address: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault LP Fees History
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/lp/fees_history
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        page(int): Page number (start from 1)
        size(int): Page size (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-fees-history
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    if page:
        payload["page"] = page
    if size:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/lp/fees_history", payload=payload)


# SP related APIs
def get_sv_sp_info(self, vault_id: Optional[str] = None, address: Optional[str] = None):
    """Get Strategy Vault SP Info
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/sp/info
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-sp-info
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    return self._request("GET", "/v1/public/strategy_vault/sp/info", payload=payload)


def get_sv_sp_transaction_history(self, vault_id: Optional[str] = None, address: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault SP Transaction History
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/sp/transaction_history
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        page(int): Page number (start from 1)
        size(int): Page size (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-sp-transaction-history
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    if page:
        payload["page"] = page
    if size:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/sp/transaction_history", payload=payload)


def get_sv_sp_claim_info(self, vault_id: Optional[str] = None, address: Optional[str] = None):
    """Get Strategy Vault SP Claim Info
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/sp/claim_info
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-sp-claim-info
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    return self._request("GET", "/v1/public/strategy_vault/sp/claim_info", payload=payload)


def get_sv_sp_fees_history(self, vault_id: Optional[str] = None, address: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault SP Fees History
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/sp/fees_history
    
    Optional Args:
        vault_id(str): Vault ID
        address(str): User address
        page(int): Page number (start from 1)
        size(int): Page size (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-sp-fees-history
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if address:
        payload["address"] = address
    if page:
        payload["page"] = page
    if size:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/sp/fees_history", payload=payload)


def get_sv_fund_info(self, vault_id: Optional[str] = None):
    """Get Strategy Vault Fund Info
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/fund/info
    
    Optional Args:
        vault_id(str): Vault ID
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-fund-info
    """
    payload = {"vault_id": vault_id} if vault_id else {}
    return self._request("GET", "/v1/public/strategy_vault/fund/info", payload=payload)


def get_sv_fund_period_info(self, vault_id: Optional[str] = None, period_number: Optional[int] = None):
    """Get Strategy Vault Fund Period Info
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/fund/period_info
    
    Optional Args:
        vault_id(str): Vault ID
        period_number(int): Period number
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-fund-period-info
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if period_number:
        payload["period_number"] = period_number
    return self._request("GET", "/v1/public/strategy_vault/fund/period_info", payload=payload)


def get_sv_fund_pending_transactions(self, vault_id: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault Fund Pending Transactions
    
    Limit: 10 requests per 1 second per IP address
    
    GET /v1/public/strategy_vault/fund/pending_transactions
    
    Optional Args:
        vault_id(str): Vault ID
        page(int): Page number (start from 1)
        size(int): Page size (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-fund-pending-transactions
    """
    payload = {}
    if vault_id:
        payload["vault_id"] = vault_id
    if page:
        payload["page"] = page
    if size:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/fund/pending_transactions", payload=payload)