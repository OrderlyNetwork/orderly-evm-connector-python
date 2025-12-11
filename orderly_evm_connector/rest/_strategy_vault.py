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