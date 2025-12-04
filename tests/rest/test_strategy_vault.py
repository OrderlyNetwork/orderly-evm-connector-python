import unittest
from unittest.mock import patch
from orderly_evm_connector.rest import Rest

class TestStrategyVaultAPI(unittest.TestCase):
    
    def setUp(self):
        self.client = Rest(
            orderly_key="test_key",
            orderly_secret="test_secret",
            orderly_account_id="test_account_id",
            wallet_secret="test_wallet_secret",
            orderly_testnet=True
        )

    @patch('orderly_evm_connector.api.API._request')
    def test_get_strategy_vault_nonce(self, mock_request):
        # Arrange
        mock_response = {
            "success": True,
            "data": {
                "nonce": 14001212121234
            },
            "timestamp": 1702989203989
        }
        mock_request.return_value = mock_response
        
        # Act
        result = self.client.get_strategy_vault_nonce()
        
        # Assert
        mock_request.assert_called_once_with("GET", "/v1/public/sv_nonce")
        self.assertEqual(result, mock_response)

    @patch('orderly_evm_connector.api.API._sign_request')
    def test_submit_sv_operation_request(self, mock_sign_request):
        # Arrange
        mock_response = {"success": True, "data": {"result": "success"}}
        mock_sign_request.return_value = mock_response

        # Act
        result = self.client.submit_sv_operation_request(
            payload_type=0,  # LP_DEPOSIT
            nonce="test_nonce",
            receiver="test_receiver",
            amount="1000000000000000000",
            vault_id="test_vault",
            token="ETH",
            dex_broker_id="test_broker",
            chain_id=1,
            chain_type="ethereum",
            signature="test_signature",
            user_address="test_user_address",
            verifying_contract="test_contract"
        )

        # Assert
        expected_message = {
            "payloadType": 0,
            "nonce": "test_nonce",
            "receiver": "test_receiver",
            "amount": "1000000000000000000",
            "vaultId": "test_vault",
            "token": "ETH",
            "dexBrokerId": "test_broker",
            "chainId": 1,
            "chainType": "ethereum"
        }

        mock_sign_request.assert_called_once_with(
            "POST",
            "/v1/sv_operation_request",
            payload={
                "message": expected_message,
                "signature": "test_signature",
                "userAddress": "test_user_address",
                "verifyingContract": "test_contract"
            }
        )
        self.assertEqual(result, mock_response)

    @patch('orderly_evm_connector.api.API._sign_request')
    def test_get_account_strategy_vault_transaction_history(self, mock_sign_request):
        # Arrange
        mock_response = {
            "success": True,
            "data": {
                "rows": [
                    {
                        "vault_id": "test_vault_id",
                        "created_time": 1734652800000,
                        "type": "withdrawal",
                        "status": "pending",
                        "amount_change": 100,
                        "asset": "USDC",
                        "shares_change": 88.009
                    }
                ],
                "meta": {
                    "total": 9,
                    "records_per_page": 25,
                    "current_page": 1
                }
            },
            "timestamp": 1702989203989
        }
        mock_sign_request.return_value = mock_response
        
        # Act
        result = self.client.get_account_strategy_vault_transaction_history(
            vault_id="test_vault_id",
            type="withdrawal",
            status="pending",
            start_t=1700000000000,
            end_t=1710000000000,
            page=1,
            size=25
        )
        
        # Assert
        mock_sign_request.assert_called_once_with(
            "GET", 
            "/v1/account_sv_transaction_history", 
            payload={
                "vault_id": "test_vault_id",
                "type": "withdrawal",
                "status": "pending",
                "start_t": 1700000000000,
                "end_t": 1710000000000,
                "page": 1,
                "size": 25
            }
        )
        self.assertEqual(result, mock_response)
    
    @patch('orderly_evm_connector.api.API._sign_request')
    def test_get_account_strategy_vault_transaction_history_with_defaults(self, mock_sign_request):
        # Arrange
        mock_response = {
            "success": True,
            "data": {
                "rows": [],
                "meta": {
                    "total": 0,
                    "records_per_page": 25,
                    "current_page": 1
                }
            },
            "timestamp": 1702989203989
        }
        mock_sign_request.return_value = mock_response
        
        # Act
        result = self.client.get_account_strategy_vault_transaction_history()
        
        # Assert
        mock_sign_request.assert_called_once_with(
            "GET", 
            "/v1/account_sv_transaction_history", 
            payload={
                "vault_id": None,
                "type": None,
                "status": None,
                "start_t": None,
                "end_t": None,
                "page": None,
                "size": None
            }
        )
        self.assertEqual(result, mock_response)

if __name__ == '__main__':
    unittest.main()