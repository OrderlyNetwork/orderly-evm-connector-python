# Orderly Open API Connector Python
[![PyPI version](https://img.shields.io/pypi/v/Pypi )](https://pypi.python.org/pypi/Pypi)
[![Python version](https://img.shields.io/badge/Python-3.10-bright)](https://www.python.org/downloads/)
[![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://github.com/OrderlyNetwork/orderly-evm-connector-python)
[![Code Style](https://img.shields.io/badge/code_style-black-black)](https://black.readthedocs.io/en/stable/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Orderly Open API Connector Python is a connector to [Orderly open API](https://orderly.network/docs/build-on-evm/evm-api/introduction)

- Supported APIs:
    - Public API Endpoints
    - Private API Endpoints
    - Websockets API Endpoints
- Inclusion of test cases and examples
- Client for both Mainnet and Testnet
- Utility methods needed for connecting Orderly Endpoints such as authentication

Note: This connector is for Orderly EVM. It is not compatible with Orderly NEAR.

## Installation

```bash
pip install orderly-evm-connector
```

## Documentation

[https://orderly.network/docs/build-on-evm/building-on-evm](https://orderly.network/docs/build-on-evm/building-on-evm)

## RESTful APIs

Usage examples:
```python
from orderly_evm_connector.rest import Rest as Client
from orderly_evm_connector.lib.utils import get_account_info

(
    orderly_key,
    orderly_secret,
    orderly_account_id,
    orderly_testnet,
    wss_id,
) = get_account_info()
client = Client(
    orderly_key=orderly_key,
    orderly_secret=orderly_secret,
    orderly_account_id=orderly_account_id,
    orderly_testnet=True,
    timeout=5
)

# Orders APIs
response = client.create_order(
    symbol="PERP_NEAR_USDC",
    order_type="LIMIT",
    side="BUY",
    order_price=1.95,
    order_quantity=1,
)
```
Please find `examples` folder to check for more endpoints.
- In order to set your Orderly Key and Orderly Secret for use of the examples, create a file `examples/config.ini` with your keys.
- Eg:
    ```ini
    # examples/config.ini
    [keys]
    orderly_key=ed25519:xxxx
    orderly_secret=ed25519:xxxx
    orderly_account_id=0xaaaa
    orderly_testnet=False
    wallet_secret=xxxx
    wss_id=ClientID
    debug=False
    ```
### Display logs

Setting the `debug=True` will log the request URL, payload and response text.

### Authentication

Requests to Orderly API needs to be signed using `orderly-key` and `orderly-secret`. 
Orderly Network uses the `ed25519` elliptic curve standard for request authentication. The `lib.utils` class provides methods for signing and generating request signatures.

```python
from orderly_evm_connector.lib.utils import generate_signature

orderly_secret = "YOUR_ORDERLY_SECRET_HERE"

# A normalized orderly request string, see Authentication section of the Orderly API Doc for details
request_str = """1649920583000POST/v1/order{"symbol": "SPOT_NEAR_USDC", "order_type": "LIMIT", "order_price": 15.23, "order_quantity": 23.11, "side": "BUY"}"""
sginature = generate_signature(orderly_secret, request_str)
```

###  Heartbeat

Once connected, the websocket server sends a ping frame every 10 seconds and is asked to return a response pong frame within 1 minute. This package automatically handles pong responses.

### Reconnect

Once the connection is abnormal, the websocket connection tries a maximum of 30 times every 5s`(WEBSOCKET_RETRY_SLEEP_TIME = 5`,`WEBSOCKET_FAILED_MAX_RETRIES = 30`). After the connection is established, the subscription is completed again


### Testnet
When creating a Rest or Websocket client, set the `orderly_testnet` parameter to true to use Testnet.

```python
orderly_testnet = True

# Private Websocket Client on Testnet
wss_client = WebsocketPrivateAPIClient(
    orderly_testnet=orderly_testnet,
    orderly_account_id=orderly_account_id,
    wss_id=wss_id,
    orderly_key=orderly_key,
    orderly_secret=orderly_secret,
    on_message=message_handler,
    on_close=on_close,
)

# Private REST API Client
client = Client(
    orderly_key=orderly_key,
    orderly_secret=orderly_secret,
    orderly_account_id=orderly_account_id,
    orderly_testnet=orderly_testnet,
    timeout=5
)
```

### Error

There are 2 types of error returned from the library:
- `orderly_evm_connector.error.ClientError`
    - This is thrown when server returns `4XX`, it's an issue from client side.
    - It has 5 properties:
        - `status_code` - HTTP status code
        - `error_code` - Server's error code, e.g. `-1102`
        - `error_message` - Server's error message, e.g. `Unknown order sent.`
        - `header` - Full response header.
        - `error_data`* - Additional detailed data which supplements the `error_message`.
            - **Only applicable on select endpoints, eg. `cancelReplace`*
- `orderly_evm_connector.error.ServerError`
    - This is thrown when server returns `5XX`, it's an issue from server side.
In addition, there are 3 types of Parameter Error:
- `orderly_evm_connector.error.ParameterRequiredError`
    - This error is thrown when a required parameter for the endpoint is not present in the request.
- `orderly_evm_connector.error.ParameterValueError`
    - This error is thrown when a value passed in for an ENUM type parameter is invalid. For example the `order_type` parameter is an ENUM with a fixed set of values users could pass in. Passing a value out of the ENUM definition will result in this error.
- `orderly_evm_connector.error.ParameterTypeError`
    - This error is thrown when a value passed in is not in consistency with the type definition of the parameter.
Websocket Client has 1 type of Error:
- `WebsocketClientError`
    - This error is thrown when there is an exception thrown by the WebsocketClient class.

## Websocket

### Websocket Client

Orderly has two Websocket endpoints, the Market Data Base Endpoint(public endpoint) and the Private User Data Stream Base Endpoint(private endpoint).
`orderly-connector` supports connecting to both endpoints in both Mainnet and Testnet. See below for example:

```python
from orderly_evm_connector.lib.utils import get_account_info
import time, logging
from orderly_evm_connector.websocket.websocket_api import WebsocketPublicAPIClient

(
    orderly_key,
    orderly_secret,
    orderly_account_id,
    orderly_testnet,
    wss_id,
) = get_account_info()


def on_close(_):
    logging.info("Do custom stuff when connection is closed")


def message_handler(_, message):
    logging.info(message)


# Public websocket does not need to pass orderly_key and orderly_secret arguments

wss_client = WebsocketPublicAPIClient(
    orderly_testnet=orderly_testnet,
    orderly_account_id=orderly_account_id,
    wss_id=wss_id,
    on_message=message_handler,
    on_close=on_close,
)

wss_client.get_24h_tickers()
time.sleep(1)
wss_client.close()
```

For private endpoint, user will need to pass in the `orderly_key` and `orderly_secret` to the `orderly.websocket.WebsocketPrivateAPIClient` class.
Private endpoint also requires signature of the message sent using `orderly_key` and `orderly_secret`. This function is encapsulated by the `WebsocketPrivateAPIClient` class. See Orderly API Docs for more detai. 
```python
wss_client = WebsocketPrivateAPIClient(
    orderly_testnet=orderly_testnet,
    orderly_account_id=orderly_account_id,
    wss_id=wss_id,
    orderly_key=orderly_key,
    orderly_secret=orderly_secret,
    on_message=message_handler,
    on_close=on_close,
)
# wss_client.get_liquidator_liquidations()
wss_client.get_notifications()
time.sleep(1)
wss_client.stop()
```


#### wss_id
`wss_id` is the request id of included in each of websocket request to orderly. This is defined by user and has a max length of 64 bytes.


## Limitation

## Contributing

Contributions are welcome.<br/>
If you've found a bug within this project, please open an issue to discuss what you would like to change.<br/>
If it's an issue with the API, please open a topic at [Orderly Developer Community]()
