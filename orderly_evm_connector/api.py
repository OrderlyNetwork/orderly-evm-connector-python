import json
from json import JSONDecodeError
import requests
from .__version__ import __version__
from orderly_evm_connector.error import ClientError, ServerError
from orderly_evm_connector.lib.utils import (
    generate_signature,
    generate_wallet_signature,
)
from orderly_evm_connector.lib.utils import cleanNoneValue
from orderly_evm_connector.lib.utils import orderlyLog, get_endpoints

class API(object):
    def __init__(
        self,
        orderly_key=None,
        orderly_secret=None,
        wallet_secret=None,
        orderly_testnet=False,
        orderly_account_id=None,
        proxies=None,
        timeout=None,
        debug=False
    ):
        self.orderly_key = orderly_key
        self.orderly_secret = orderly_secret
        self.wallet_secret = wallet_secret
        self.orderly_endpoint, _, _ = get_endpoints(orderly_testnet)
        self.orderly_account_id = orderly_account_id
        self.timeout = timeout
        self.show_header = False
        self.proxies = proxies
        self.logger = orderlyLog(debug=debug)
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
                "User-Agent": "orderly-connector-python/" + __version__,
            }
        )
        return

    def _request(self, http_method, url_path, payload=None):
        if payload:
            _payload = cleanNoneValue(payload)
            if _payload:
                if http_method == "GET" or http_method == "DELETE":
                    url_path += "?" + "&".join(
                        [f"{k}={v}" for k, v in _payload.items()]
                    )
                    payload = ""
                else:
                    payload = _payload

        if payload is None:
            payload = ""
        url = self.orderly_endpoint + url_path
        self.logger.debug("url: " + url)
        params = cleanNoneValue(
            {
                "url": url,
                "params": payload,
                "timeout": self.timeout,
                "proxies": self.proxies,
            }
        )
        response = self._dispatch_request(http_method, params)
        self.logger.debug("raw response from server:" + response.text)
        self._handle_rest_exception(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text

        return data

    def get_wallet_signature(self, message=None):
        return generate_wallet_signature(self.wallet_secret, message=message)

    def _sign_request(self, http_method, url_path, payload=None):
        _payload = ""
        if payload:
            _payload = cleanNoneValue(payload)
            if _payload:
                if http_method == "GET" or http_method == "DELETE":
                    url_path += "?" + "&".join(
                        [f"{k}={v}" for k, v in _payload.items()]
                    )
                    _payload = ""
        params = {}
        payload = _payload if _payload else ""
        params["url_path"] = url_path
        params["payload"] = payload
        params["http_method"] = http_method
        query_string = self._prepare_params(params)
        try:
            _timestamp, _signature = generate_signature(
                self.orderly_secret, message=query_string
            )
        except ValueError:
            _timestamp, _signature = "mock_timestamp", "mock_signature"

        self.session.headers.update(
            {
                "orderly-timestamp": _timestamp,
                "orderly-account-id": self.orderly_account_id,
                "orderly-key": self.orderly_key,
                "orderly-signature": _signature,
            }
        )
        self.logger.debug(f"Sign Request Headers: {self.session.headers}")
        return self.send_request(http_method, url_path, payload)

    def send_request(self, http_method, url_path, payload=None):
        if payload is None:
            payload = {}
        url = self.orderly_endpoint + url_path
        self.logger.debug("url: " + url)
        params = cleanNoneValue(
            {
                "url": url,
                "params": payload,
                "timeout": self.timeout,
                "proxies": self.proxies,
            }
        )
        response = self._dispatch_request(http_method, params)
        self.logger.debug("raw response from server:" + response.text)
        self._handle_rest_exception(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text
        result = {}

        if self.show_header:
            result["header"] = response.headers

        if len(result) != 0:
            result["data"] = data
            return result
        return data

    def _prepare_params(self, params: dict):
        _http_method = params["http_method"]
        _url_path = params["url_path"]
        _payload = (
            json.dumps(params["payload"]) if params["payload"] else params["payload"]
        )
        _params = "{0}{1}{2}".format(_http_method, _url_path, _payload)
        return _params

    def _dispatch_request(self, http_method, params):
        method_func = {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method, "GET")
        if http_method == "POST" or http_method == "PUT":
            self.session.headers.update(
                {
                    "Content-Type": "application/json;charset=utf-8"
                }
            )
            return method_func(url=params["url"], json=params["params"])
        else:
            self.session.headers.update(
                {
                    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
                }
            )
            return method_func(url=params["url"])

    def _handle_rest_exception(self, response):
        status_code = response.status_code
        if status_code <= 400:
            return
        if 400 < status_code < 500:
            try:
                err = json.loads(response.text)
            except JSONDecodeError:
                raise ClientError(
                    status_code, None, response.text, None, response.headers
                )
            error_data = None
            if "data" in err:
                error_data = err["data"]
            raise ClientError(
                status_code, err["code"], err["message"], response.headers, error_data
            )
        raise ServerError(status_code, response.text)
