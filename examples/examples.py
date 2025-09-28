import logging
import math
from datetime import datetime, timezone

from base58 import b58encode
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from orderly_evm_connector.error import ClientError
from orderly_evm_connector.rest import Rest as Client
from utils.config import get_account_info

# logging.basicConfig(level=logging.INFO)

def encode_key(key: bytes) -> str:
    """Return the Orderly-compatible base58 string for an Ed25519 key."""

    return f"ed25519:{b58encode(key).decode('utf-8')}"


def compute_timestamps() -> tuple[int, int]:
    """Compute the current timestamp and a one-year expiration in milliseconds."""

    now = datetime.now(timezone.utc).replace(tzinfo=None)
    epoch = datetime(1970, 1, 1)
    timestamp = math.trunc((now - epoch).total_seconds() * 1_000)
    expiration = timestamp + 1_000 * 60 * 60 * 24 * 365
    return timestamp, expiration


def create_private_client(debug: bool = True) -> Client:
    (
        orderly_key,
        orderly_secret,
        orderly_account_id,
        wallet_secret,
        orderly_testnet,
        _wss_id,
    ) = get_account_info()

    return Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
        orderly_account_id=orderly_account_id,
        orderly_testnet=orderly_testnet,
        wallet_secret=wallet_secret,
        debug=debug,
    )

def main() -> None:
    client_private = create_private_client()

    new_orderly_key = Ed25519PrivateKey.generate()
    pub_new_orderly_key = encode_key(new_orderly_key.public_key().public_bytes_raw())
    timestamp, expiration = compute_timestamps()

    logging.info("Generated new orderly public key: %s", pub_new_orderly_key)
    logging.info("Timestamp: %s, Expiration: %s", timestamp, expiration)

    # client_private.add_orderly_key(
    #     "woofi_pro",
    #     421614,
    #     pub_new_orderly_key,
    #     "read,trading,asset",
    #     timestamp,
    #     expiration,
    #     "0xF7c02b690083Be14c13C7f96561db289aa67Fb70",
    # )
    client_private.remove_orderly_key("ed25519:J1oenwuQVu2fLqStzhiFCiK9CcsUhRFAFp7EvcM1cPyZ")

if __name__ == "__main__":
    main()
