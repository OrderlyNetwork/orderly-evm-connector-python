from orderly_evm_connector.rest import Rest as Client
from utils.config import get_account_info

from base58 import b58encode
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from datetime import datetime, timezone
import math


(
    orderly_key,
    orderly_secret,
    orderly_account_id,
    wallet_secret,
    orderly_testnet,
    wss_id,
) = get_account_info()

client_private = Client(
    orderly_key=orderly_key,
    orderly_secret=orderly_secret,
    orderly_account_id=orderly_account_id,
    orderly_testnet=orderly_testnet,
    wallet_secret=wallet_secret,
    debug=True
)

def encode_key(key: bytes):
    return "ed25519:%s" % b58encode(key).decode("utf-8")

new_orderly_key = Ed25519PrivateKey.generate()

pub_new_orderly_key = encode_key(new_orderly_key.public_key().public_bytes_raw())

d = datetime.now(timezone.utc).replace(tzinfo=None)
epoch = datetime(1970, 1, 1)
timestamp = math.trunc((d - epoch).total_seconds() * 1_000)
expiration = timestamp + 1_000 * 60 * 60 * 24 * 365
userAddress = "0xF7c02b690083Be14c13C7f96561db289aa67Fb70"

# client_private.add_orderly_key(
#     "woofi_pro",
#     421614,
#     pub_new_orderly_key,
#     "read,trading,asset",
#     timestamp,
#     expiration,
#     userAddress
# )

client_private.remove_orderly_key("ed25519:J1oenwuQVu2fLqStzhiFCiK9CcsUhRFAFp7EvcM1cPyZ")
