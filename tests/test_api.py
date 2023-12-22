from orderly.api import API
from orderly.error import ClientError, ServerError
from orderly.rest import Rest as Client
from orderly.lib.utils import orderlyLog, get_endpoints
from orderly.__version__ import __version__
import requests, responses
from tests.utils import random_str, mock_http_response


mock_item = {"key_1": "value_1", "key_2": "value_2"}

def test_API_initial():
    """Tests the API initialization"""

    client = API()

    client.should.be.a(API)
    client.orderly_key.should.be.none
    client.timeout.should.be.none
    client.orderly_secret.should.be.none
    client.wallet_secret.should.be.none
    client.orderly_account_id.should.be.none
    client.show_header.should.be.false
    client.session.should.be.a(requests.Session)
    client.session.headers.should.have.key("Content-Type").which.should.equal(
        "application/json;charset=utf-8"
    )
    client.session.headers.should.have.key("User-Agent").which.should.equal(
        "orderly-connector-python/" + __version__
    )


def test_API_with_extra_parameters():
    """Tests the API initialization with extra parameters"""

    orderly_key = random_str()
    orderly_secret = random_str()
    wallet_secret = random_str()
    orderly_account_id = random_str()
    proxies = {"https": "https://1.2.3.4:8080"}

    client = Client(
        orderly_key=orderly_key,
        orderly_secret=orderly_secret,
        orderly_testnet=True,
        wallet_secret=wallet_secret,
        orderly_account_id=orderly_account_id,
        proxies=proxies
    )

    client.should.be.a(Client)
    client.orderly_key.should.equal(orderly_key)
    client.orderly_endpoint.should.equal(get_endpoints(True)[0])
    client.orderly_secret.should.equal(orderly_secret)
    client.orderly_account_id.should.equal(orderly_account_id)
    client.wallet_secret.should.equal(wallet_secret)
    client.proxies.should.equal(proxies)


def test_API_with_none_time_out():
    client = API(timeout=None)
    client.timeout.should.be.none
    client = API()
    client.timeout.should.be.none


def test_API_with_illegal_proxies():
    client = API(proxies="aaa")
    client.proxies.should.be.none


@mock_http_response(responses.GET, "/test/throw/client/error", None, 402)
def test_throw_client_error():
    client = API()
    client.send_request.when.called_with(
        "GET", "/test/throw/client/error"
    ).should.throw(ClientError)


@mock_http_response(responses.GET, "/test/throw/server/error", mock_item, 502)
def test_throw_server_error():
    client = API()
    client.send_request.when.called_with(
        "GET", "/test/throw/server/error"
    ).should.throw(ServerError)
