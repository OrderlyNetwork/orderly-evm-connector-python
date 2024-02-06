from orderly_evm_connector.lib.utils import check_required_parameters, get_timestamp
from orderly_evm_connector.lib.utils import check_enum_parameter,get_withdraw_settle_verifyingcontract
from orderly_evm_connector.lib.enums import WalletSide, AssetStatus


def delegate_signer(
    self, delegateContract: str, brokerId: str, chainId: int, registrationNonce: int, txHash: str, timestamp: int, userAddress: str
):
    """
    Delegate Signer

    Limit: 1 requests per 1 second

    POST /v1/delegate_signer

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/add-delegate-signer
    """
    _message = {
        "delegateContract": delegateContract,
        "brokerId": brokerId,
        "chainId": chainId,
        "registrationNonce": registrationNonce,
        "txHash": txHash,
        "timestamp": timestamp
    }

    message = {
        "domain": {
            "name": "Orderly",
            "version": "1",
            "chainId": chainId,
            "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC",
        },
        "message": _message,
        "primaryType": "DelegateSigner",
        "types": {
            "EIP712Domain": [
                {"name": "name", "type": "string"},
                {"name": "version", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "verifyingContract", "type": "address"},
            ],
            "DelegateSigner": [
                {"name": "delegateContract", "type": "address"},
                {"name": "brokerId", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "timestamp", "type": "uint64"},
                {"name": "registrationNonce", "type": "uint256"},
                {"name": "txHash", "type": "bytes32"},
            ],
        },
    }

    _signature = self.get_wallet_signature(message=message)
    payload = {"message": _message, "signature": _signature, "userAddress": userAddress}
    check_required_parameters(
        [
            [brokerId, "brokerId"],
            [chainId, "chainId"],
            [registrationNonce, "registrationNonce"],
            [userAddress, "userAddress"],
        ]
    )
    return self._request("POST", "/v1/delegate_signer", payload=payload)


def delegate_add_orderly_key(
    self,
    delegateContract: str,
    brokerId: str,
    chainId: int,
    orderlyKey: str,
    scope: str,
    timestamp: int,
    expiration: int,
    userAddress: str,
    **kwargs
):
    """
    Delegate Orderly Key

    Limit: 1 requests per 1 second

    POST /v1/delegate_orderly_key

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/delegate_orderly_key
    """
    _message = {
        "delegateContract": delegateContract,
        "brokerId": brokerId,
        "chainId": chainId,
        "orderlyKey": orderlyKey,
        "scope": scope,
        "timestamp": timestamp,
        "expiration": expiration,
    }
    message = {
        "domain": {
            "name": "Orderly",
            "version": "1",
            "chainId": chainId,
            "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC",
        },
        "message": _message,
        "primaryType": "DelegateAddOrderlyKey",
        "types": {
            "EIP712Domain": [
                {"name": "name", "type": "string"},
                {"name": "version", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "verifyingContract", "type": "address"},
            ],
            "AddOrderlyKey": [
                {"name": "delegateContract", "type": "address"},
                {"name": "brokerId", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "orderlyKey", "type": "string"},
                {"name": "scope", "type": "string"},
                {"name": "timestamp", "type": "uint64"},
                {"name": "expiration", "type": "uint64"},
            ],
        },
    }
    _signature = self.get_wallet_signature(message=message)
    payload = {
        "message": _message,
        "signature": _signature,
        "userAddress": userAddress,
        **kwargs,
    }
    check_required_parameters(
        [
            [brokerId, "brokerId"],
            [chainId, "chainId"],
            [orderlyKey, "orderlyKey"],
            [scope, "scope"],
            [timestamp, "timestamp"],
            [expiration, "expiration"],
            [userAddress, "userAddress"],
        ]
    )
    return self._request("POST", "/v1/delegate_orderly_key", payload=payload)


def delegate_withdraw_request(
    self,
    delegateContract: int,
    userAddress: str,
    brokerId: str,
    chainId: int,
    receiver: str,
    token: str,
    amount: str,
    withdrawNonce: int,
    timestamp: int
):
    """
    Delegate Withdraw Request

    Limit: 1 requests per 1 second

    POST /v1/delegate_withdraw_request

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/delegate_withdraw_request
    """
    check_required_parameters(
        [
            [brokerId, "brokerId"],
            [chainId, "chainId"],
            [receiver, "receiver"],
            [token, "token"],
            [amount, "amount"],
            [withdrawNonce, "withdrawNonce"],
            [timestamp, "timestamp"],
            [delegateContract, "delegateContract"]
        ]
    )
    _message = {
        "brokerId": brokerId,
        "chainId": chainId,
        "receiver": receiver,
        "token": token,
        "amount": amount,
        "withdrawNonce": withdrawNonce,
        "timestamp": timestamp,
        "delegateContract": delegateContract,
    }
    verifyingContract = get_withdraw_settle_verifyingcontract(self.orderly_testnet)
    message = {
        "domain": {
            "name": "Orderly",
            "version": "1",
            "chainId": chainId,
            "verifyingContract": verifyingContract,
        },
        "message": _message,
        "primaryType": "DelegateWithdraw",
        "types": {
            "EIP712Domain": [
                {"name": "name", "type": "string"},
                {"name": "version", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "verifyingContract", "type": "address"},
            ],
            "DelegateWithdraw": [
                {"name": "delegateContract", "type": "string"},
                {"name": "brokerId", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "receiver", "type": "address"},
                {"name": "token", "type": "string"},
                {"name": "amount", "type": "uint256"},
                {"name": "withdrawNonce", "type": "uint64"},
                {"name": "timestamp", "type": "uint64"},
            ],
        },
    }
    _signature = self.get_wallet_signature(message=message)
    payload = {
        "message": _message,
        "signature": _signature,
        "userAddress": userAddress,
        "verifyingContract": verifyingContract,
    }
    return self._sign_request("POST", "/v1/delegate_withdraw_request", payload=payload)


def delegate_request_pnl_settlement(
    self,
    delegateContract: int,
    brokerId: str,
    chainId: int,
    settleNonce: int,
    userAddress: str,
    timestamp: int
):
    """
    Delegate Orderly Key

    Limit: 1 requests per 1 second

    POST /v1/delegate_settle_pnl

    https://docs.orderly.network/build-on-evm/evm-api/restful-api/public/delegate_settle_pnl
    """
    check_required_parameters(
        [
            [delegateContract, "delegateContract"],
            [brokerId, "brokerId"],
            [chainId, "chainId"],
            [settleNonce, "settleNonce"],
            [userAddress, "userAdress"],
            [timestamp, "timestamp"],
        ]
    )
    verifyingContract = get_withdraw_settle_verifyingcontract(self.orderly_testnet)
    _message = {
        "delegateContract": delegateContract,
        "brokerId": brokerId,
        "chainId": chainId,
        "settleNonce": settleNonce,
        "timestamp": timestamp,
    }
    message = {
        "domain": {
            "name": "Orderly",
            "version": "1",
            "chainId": chainId,
            "verifyingContract": verifyingContract,
        },
        "message": _message,
        "primaryType": "DelegateSettlePnl",
        "types": {
            "EIP712Domain": [
                {"name": "name", "type": "string"},
                {"name": "version", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "verifyingContract", "type": "address"},
            ],
            "DelegateSettlePnl": [
                {"name": "delegateContract", "type": "address"},
                {"name": "brokerId", "type": "string"},
                {"name": "chainId", "type": "uint256"},
                {"name": "settleNonce", "type": "uint64"},
                {"name": "timestamp", "type": "uint64"},
            ],
        },
    }

    _signature = self.get_wallet_signature(message=message)
    payload = {
        "message": _message,
        "signature": _signature,
        "userAddress": userAddress,
        "verifyingContract": verifyingContract,
    }
    return self._sign_request("POST", "/v1/delegate_settle_pnl", payload=payload)
