from typing import Optional
from orderly_evm_connector.lib.enums import SVPayloadType
from orderly_evm_connector.lib.utils import check_required_parameters

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


def trigger_manual_period_delivery(self, plan_id: str):
    """Trigger Manual Period Delivery

    Limit: 1 request per second per account

    POST /v1/sv/manual_period_delivery

    Args:
        plan_id(string): Plan ID

    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/private/trigger-manual-period-delivery
    """
    check_required_parameters([
        [plan_id, "plan_id"]
    ])

    payload = {"plan_id": plan_id}
    return self._sign_request("POST", "/v1/sv/manual_period_delivery", payload=payload)


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
def get_sv_vault_info(self, vault_id: Optional[str] = None, status: Optional[str] = None, broker_ids: Optional[str] = None):
    """Get Strategy Vault Info
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/vault/info
    
    Optional Args:
        vault_id(str): Vault ID (return all if empty)
        status(str): return all if no filter
        broker_ids(str): can filter multiple broker_id per query
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-info
    """
    payload = {}
    if vault_id is not None:
        payload["vault_id"] = vault_id
    if status is not None:
        payload["status"] = status
    if broker_ids is not None:
        payload["broker_ids"] = broker_ids
    return self._request("GET", "/v1/public/strategy_vault/vault/info", payload=payload)


def get_sv_vault_overall_info(self, broker_ids: Optional[str] = None):
    """Get Overall Statistics of all Strategy Vaults
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/vault/overall_info
    
    Optional Args:
        broker_ids(str): return all if no filter. can filter multiple broker_id per query
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-overall-info
    """
    payload = {}
    if broker_ids is not None:
        payload["broker_ids"] = broker_ids
    return self._request("GET", "/v1/public/strategy_vault/vault/overall_info", payload=payload)


def get_sv_user_overall_info(self, wallet_address: str):
    """Get User Overall Statistics across Strategy Vaults
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/user/overall_info
    
    Args:
        wallet_address(str): Wallet address (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-user-overall-info
    """
    check_required_parameters([
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "wallet_address": wallet_address
    }
    return self._request("GET", "/v1/public/strategy_vault/user/overall_info", payload=payload)


def get_sv_vault_performance(self, vault_id: str):
    """Get Strategy Vault Performance
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/vault/performance
    
    Args:
        vault_id(str): Vault ID (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-performance
    """
    check_required_parameters([
        [vault_id, "vault_id"]
    ])
    payload = {
        "vault_id": vault_id
    }
    return self._request("GET", "/v1/public/strategy_vault/vault/performance", payload=payload)


def get_sv_vault_performance_chart(self, vault_id: str, type: str, time_range: str):
    """Get Strategy Vault TVL/PnL History
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/vault/performance_chart
    
    Args:
        vault_id(str): Vault ID (required)
        type(str): `PNL` / `TVL` (required)
        time_range(str): `24h` / `7d` / `30d` / `all_time` (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-performance-chart
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [type, "type"],
        [time_range, "time_range"]
    ])
    payload = {
        "vault_id": vault_id,
        "type": type,
        "time_range": time_range
    }
    return self._request("GET", "/v1/public/strategy_vault/vault/performance_chart", payload=payload)


def get_sv_vault_positions(self, vault_id: str):
    """Get Strategy Vault Positions
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/vault/positions
    
    Args:
        vault_id(str): Vault ID (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-positions
    """
    check_required_parameters([
        [vault_id, "vault_id"]
    ])
    payload = {
        "vault_id": vault_id
    }
    return self._request("GET", "/v1/public/strategy_vault/vault/positions", payload=payload)


def get_sv_vault_open_orders(self, vault_id: str, symbol: Optional[str] = None, sort_by: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault Open Orders
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/vault/open_orders
    
    Includes both normal & algo orders
    
    Args:
        vault_id(str): Vault ID (required)
        
    Optional Args:
        symbol(str): one symbol at a time
        sort_by(str): `ascending` / `descending` (default) on updated_time
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-open-orders
    """
    check_required_parameters([
        [vault_id, "vault_id"]
    ])
    payload = {
        "vault_id": vault_id
    }
    if symbol is not None:
        payload["symbol"] = symbol
    if sort_by is not None:
        payload["sort_by"] = sort_by
    if page is not None:
        payload["page"] = page
    if size is not None:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/vault/open_orders", payload=payload)


def get_sv_vault_trade_history(self, vault_id: str, symbol: Optional[str] = None, sort_by: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault Trade History
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/vault/trade_history
    
    Args:
        vault_id(str): Vault ID (required)
        
    Optional Args:
        symbol(str): one symbol at a time
        sort_by(str): `ascending` / `descending` (default)
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-trade-history
    """
    check_required_parameters([
        [vault_id, "vault_id"]
    ])
    payload = {
        "vault_id": vault_id
    }
    if symbol is not None:
        payload["symbol"] = symbol
    if sort_by is not None:
        payload["sort_by"] = sort_by
    if page is not None:
        payload["page"] = page
    if size is not None:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/vault/trade_history", payload=payload)


def get_sv_vault_liquidator_history(self, vault_id: str, symbol: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault Liquidator History
    
    Liquidated positions of liquidator
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/vault/liquidator_history
    
    Args:
        vault_id(str): Vault ID (required)
        
    Optional Args:
        symbol(str): only 1 at a time
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-liquidator-history
    """
    check_required_parameters([
        [vault_id, "vault_id"]
    ])
    payload = {
        "vault_id": vault_id
    }
    if symbol is not None:
        payload["symbol"] = symbol
    if page is not None:
        payload["page"] = page
    if size is not None:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/vault/liquidator_history", payload=payload)


# LP related APIs
def get_sv_lp_info(self, wallet_address: str, vault_id: Optional[str] = None):
    """Get Liquidity Provider Info
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/lp/info
    
    Args:
        wallet_address(str): Wallet address (required)
        
    Optional Args:
        vault_id(str): Vault ID (return all if empty)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-info
    """
    check_required_parameters([
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "wallet_address": wallet_address
    }
    if vault_id is not None:
        payload["vault_id"] = vault_id
    return self._request("GET", "/v1/public/strategy_vault/lp/info", payload=payload)


def get_sv_lp_performance(self, vault_id: str, wallet_address: str):
    """Get Liquidity Provider Performance
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/lp/performance
    
    Liquidity Provider's performance in a vault
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-performance
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address
    }
    return self._request("GET", "/v1/public/strategy_vault/lp/performance", payload=payload)


def get_sv_lp_performance_chart(self, vault_id: str, wallet_address: str, type: str, time_range: str):
    """Get Liquidity Provider TVL/PnL History
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/lp/performance_chart
    
    Liquidity Provider's TVL/PnL history in a vault
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        type(str): `PNL` / `TVL` (required)
        time_range(str): `24h` / `7d` / `30d` / `all_time` (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-performance-chart
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"],
        [type, "type"],
        [time_range, "time_range"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address,
        "type": type,
        "time_range": time_range
    }
    return self._request("GET", "/v1/public/strategy_vault/lp/performance_chart", payload=payload)


def get_sv_lp_transaction_history(
    self, 
    vault_id: str, 
    wallet_address: str, 
    type: Optional[str] = None, 
    chain_id: Optional[str] = None, 
    source: Optional[str] = None,
    page: Optional[int] = None, 
    size: Optional[int] = None
):
    """Get Liquidity Provider Transaction History
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/lp/transaction_history
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        
    Optional Args:
        type(str): `deposit` / `withdrawal` / return all if empty
        chain_id(str): return all if empty
        source(str): `wallet` / `broker_id` / return all if empty
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-transaction-history
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address
    }
    if type is not None:
        payload["type"] = type
    if chain_id is not None:
        payload["chain_id"] = chain_id
    if source is not None:
        payload["source"] = source
    if page is not None:
        payload["page"] = page
    if size is not None:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/lp/transaction_history", payload=payload)


def get_sv_lp_claim_info(self, vault_id: str, wallet_address: str, chain_id: str):
    """Get Liquidity Provider Claim Info
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/lp/claim_info
    
    The claimable asset amount on a chain from the processed withdrawal request(s) of a vault
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        chain_id(str): Chain ID (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-claim-info
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"],
        [chain_id, "chain_id"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address,
        "chain_id": chain_id
    }
    return self._request("GET", "/v1/public/strategy_vault/lp/claim_info", payload=payload)


def get_sv_lp_fees_history(self, vault_id: str, wallet_address: str, page: Optional[int] = None, size: Optional[int] = None, start_t: Optional[int] = None, end_t: Optional[int] = None):
    """Get Liquidity Provider Fee History
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/lp/fees_history
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        
    Optional Args:
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        start_t(int): Start time range that wish to query
        end_t(int): End time range that wish to query
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-lp-fees-history
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address
    }
    if page is not None:
        payload["page"] = page
    if size is not None:
        payload["size"] = size
    if start_t is not None:
        payload["start_t"] = start_t
    if end_t is not None:
        payload["end_t"] = end_t
    return self._request("GET", "/v1/public/strategy_vault/lp/fees_history", payload=payload)


# SP related APIs
def get_sv_sp_info(self, vault_id: str, wallet_address: str):
    """Get Strategy Provider's Info
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/sp/info
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-sp-info
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address
    }
    return self._request("GET", "/v1/public/strategy_vault/sp/info", payload=payload)


def get_sv_sp_transaction_history(
    self, 
    vault_id: str, 
    wallet_address: str, 
    type: Optional[str] = None, 
    chain_id: Optional[str] = None, 
    source: Optional[str] = None,
    page: Optional[int] = None, 
    size: Optional[int] = None
):
    """Get Strategy Provider Transaction History
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/sp/transaction_history
    
    View Strategy Provider Transaction History
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        
    Optional Args:
        type(str): `deposit` / `withdrawal` / return all if empty
        chain_id(str): return all if empty
        source(str): `wallet` / `broker_id` / return all if empty
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-sp-transaction-history
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address
    }
    if type is not None:
        payload["type"] = type
    if chain_id is not None:
        payload["chain_id"] = chain_id
    if source is not None:
        payload["source"] = source
    if page is not None:
        payload["page"] = page
    if size is not None:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/sp/transaction_history", payload=payload)

def get_sv_vault_order_history(self, vault_id: str, symbol: Optional[str] = None, sort_by: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Vault Order History
    
    Include both normal & algo orders
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/vault/order_history
    
    Args:
        vault_id(str): Vault ID (required)
        
    Optional Args:
        symbol(str): one symbol at a time
        sort_by(str): `ascending` / `descending` (default) on updated_time
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-vault-order-history
    """
    check_required_parameters([
        [vault_id, "vault_id"]
    ])
    payload = {
        "vault_id": vault_id
    }
    if symbol is not None:
        payload["symbol"] = symbol
    if sort_by is not None:
        payload["sort_by"] = sort_by
    if page is not None:
        payload["page"] = page
    if size is not None:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/vault/order_history", payload=payload)


def get_sv_sp_claim_info(self, vault_id: str, wallet_address: str, chain_id: str):
    """Get Strategy Provider Claimable Amount
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/sp/claim_info
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        chain_id(str): Chain ID (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-sp-claim-info
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"],
        [chain_id, "chain_id"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address,
        "chain_id": chain_id
    }
    return self._request("GET", "/v1/public/strategy_vault/sp/claim_info", payload=payload)


def get_sv_sp_fees_history(self, vault_id: str, wallet_address: str, page: Optional[int] = None, size: Optional[int] = None):
    """Get Strategy Provider Fee History
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/sp/fees_history
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        
    Optional Args:
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-sp-fees-history
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address
    }
    if page is not None:
        payload["page"] = page
    if size is not None:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/sp/fees_history", payload=payload)


def get_sv_fund_info(self, vault_id: str, wallet_address: str):
    """Get Strategy Fund Details
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/fund/info
    
    View Strategy Fund Info
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-fund-info
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address
    }
    return self._request("GET", "/v1/public/strategy_vault/fund/info", payload=payload)


def get_sv_fund_period_info(self, vault_id: str, wallet_address: str, period_number: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Get Period History and Fund Period Instructions
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/fund/period_info
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        
    Optional Args:
        period_number(str): Period number
        page(int): The page you wish to query (start from 1)
        size(int): The page size you wish to query (max: 500)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-fund-period-info
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address
    }
    if period_number is not None:
        payload["period_number"] = period_number
    if page is not None:
        payload["page"] = page
    if size is not None:
        payload["size"] = size
    return self._request("GET", "/v1/public/strategy_vault/fund/period_info", payload=payload)


def get_sv_fund_pending_transactions(self, vault_id: str, wallet_address: str):
    """Get Preview Users Pending Requests
    
    Limit: 10 requests per second per IP address
    
    GET /v1/public/strategy_vault/fund/pending_transactions
    
    Args:
        vault_id(str): Vault ID (required)
        wallet_address(str): Wallet address (required)
        
    https://orderly.network/docs/build-on-omnichain/evm-api/restful-api/public/get-strategy-vault-fund-pending-transactions
    """
    check_required_parameters([
        [vault_id, "vault_id"],
        [wallet_address, "wallet_address"]
    ])
    payload = {
        "vault_id": vault_id,
        "wallet_address": wallet_address
    }
    return self._request("GET", "/v1/public/strategy_vault/fund/pending_transactions", payload=payload)