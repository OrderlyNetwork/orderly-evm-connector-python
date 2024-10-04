import json
import os
import time
import uuid
import pathlib
from configparser import ConfigParser
from urllib.parse import urlparse
from collections import OrderedDict
from urllib.parse import urlencode
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from eth_account.messages import encode_structured_data
from web3 import Web3
import base58,base64
import logging
from orderly_evm_connector.error import (
    ParameterRequiredError,
    ParameterValueError,
    ParameterTypeError,
)


import logging
initialized = False
disable_validation = os.environ.get("DISABLE_VALIDATION", False)
test_url = os.environ.get("ORDERLY_TEST_URL", False)
def orderlyLog(debug=False):
    
    logger = logging.getLogger("orderly_log")
    if not logger.handlers:
        if debug:
            logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
        else:
            logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")
    return logger



def cleanNoneValue(d) -> dict:
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out


def check_required_parameter(value, name):
    if not value and value != 0:
        raise ParameterRequiredError([name])


def check_required_parameters(params):
    """Validate multiple parameters
    params = [
        ['PERP_BTC_USDC', 'symbol'],
        [10, 'price']
    ]
    """
    if not disable_validation:
        for p in params:
            check_required_parameter(p[0], p[1])


def check_enum_parameter(value, enum_class):
    if not disable_validation:
        if value not in set(item.value for item in enum_class):
            raise ParameterValueError([value])


def check_type_parameter(value, name, data_type):
    if value is not None and not isinstance(value, data_type):
        raise ParameterTypeError([name, data_type])


def get_timestamp():
    return int(time.time() * 1000)


def convert_list_to_json_array(symbols):
    if symbols is None:
        return symbols
    res = json.dumps(symbols)
    return res.replace(" ", "")


def get_uuid():
    return str(uuid.uuid4())


def purge_map(map: map):
    """Remove None values from map"""
    return {k: v for k, v in map.items() if v is not None and v != "" and v != 0}


def parse_proxies(proxies: dict):
    """Parse proxy url from dict, only support http and https proxy, not support socks5 proxy"""
    proxy_url = proxies.get("http") or proxies.get("https")
    if not proxy_url:
        return {}

    parsed = urlparse(proxy_url)
    return {
        "http_proxy_host": parsed.hostname,
        "http_proxy_port": parsed.port,
        "http_proxy_auth": (parsed.username, parsed.password)
        if parsed.username and parsed.password
        else None,
    }


def generate_signature(orderly_secret, message=None):
    if not orderly_secret:
        raise "Please configure orderly secret in the configuration file config.ini"
    _orderly_secret = orderly_secret.split(":")[1]
    _orderly_private_key = Ed25519PrivateKey.from_private_bytes(
        base58.b58decode(_orderly_secret)[0:32]
    )
    _timestamp = get_timestamp()
    if message and isinstance(message, dict):
        message["timestamp"] = _timestamp
    else:
        message = f"{_timestamp}{message or ''}" 
    _signature = base64.b64encode(
        _orderly_private_key.sign(bytes(message, "utf-8"))
    ).decode("utf-8")
    return str(_timestamp), _signature


def generate_wallet_signature(wallet_secret, message=None):
    private_key = f"0x{wallet_secret}"
    _message = message
    encoded_message = encode_structured_data(_message)
    w3 = Web3()
    signed_message = w3.eth.account.sign_message(
        encoded_message, private_key=private_key
    )
    return signed_message.signature.hex()


def get_endpoints(orderly_testnet):
    # True: Testnet, False: Mainnet
    if orderly_testnet and orderly_testnet.lower() == 'true':
        orderly_endpoint = test_url or "https://testnet-api-evm.orderly.org"
        orderly_websocket_public_endpoint = "wss://testnet-ws-evm.orderly.org/ws/stream"
        orderly_websocket_private_endpoint = (
            "wss://testnet-ws-private-evm.orderly.org/v2/ws/private/stream"
        )
        return (
            orderly_endpoint,
            orderly_websocket_public_endpoint,
            orderly_websocket_private_endpoint,
        )
    else:
        orderly_endpoint = "https://api-evm.orderly.org"
        orderly_websocket_public_endpoint = "wss://ws-evm.orderly.org/ws/stream"
        orderly_websocket_private_endpoint = (
            "wss://ws-private-evm.orderly.org/v2/ws/private/stream"
        )
        return (
            orderly_endpoint,
            orderly_websocket_public_endpoint,
            orderly_websocket_private_endpoint,
        )
        
def get_withdraw_settle_verifyingcontract(orderly_testnet):
    verifyingcontract  = '0x1826B75e2ef249173FC735149AE4B8e9ea10abff' if orderly_testnet else '0x6F7a338F2aA472838dEFD3283eB360d4Dff5D203'
    return verifyingcontract

def decode_ws_error_code(data):
    try:
        return str(int.from_bytes(data, byteorder='big'))
    except:
        return ""


def get_account_info():
    config = ConfigParser()
    config_file_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "..", "config.ini"
    )
    config.read(config_file_path)
    return (
        config["keys"]["orderly_key"],
        config["keys"]["orderly_secret"],
        config["keys"]["orderly_account_id"],
        config["keys"]["wallet_secret"],
        config["keys"]["orderly_testnet"],
        config["keys"]["wss_id"],
    )
