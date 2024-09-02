from json import JSONDecodeError
import aiohttp
from .__version__ import __version__
from orderly_evm_connector.error import ClientError, ServerError
from orderly_evm_connector.lib.utils import (
    generate_signature,
)
from orderly_evm_connector.lib.utils import cleanNoneValue
from .api import API  # Import the original API class

class AsyncAPI(API):
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
        super().__init__(
            orderly_key=orderly_key,
            orderly_secret=orderly_secret,
            wallet_secret=wallet_secret,
            orderly_testnet=orderly_testnet,
            orderly_account_id=orderly_account_id,
            proxies=proxies,
            timeout=timeout,
            debug=debug
        )
        self.headers = {
            "Content-Type": "application/json;charset=utf-8",
            "User-Agent": "orderly-connector-python/" + __version__,
        }

    async def _request(self, http_method, url_path, payload=None):
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
        return await self._dispatch_request(http_method, params)

    async def _sign_request(self, http_method, url_path, payload=None):
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

        self.headers.update(
            {
                "orderly-timestamp": _timestamp,
                "orderly-account-id": self.orderly_account_id,
                "orderly-key": self.orderly_key,
                "orderly-signature": _signature,
            }
        )
        self.logger.debug(f"Sign Request Headers: {self.headers}")
        return await self.send_request(http_method, url_path, payload)

    async def send_request(self, http_method, url_path, payload=None):
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
        return await self._dispatch_request(http_method, params)

    async def _dispatch_request(self, http_method, params):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            method_func = {
                "GET": session.get,
                "DELETE": session.delete,
                "PUT": session.put,
                "POST": session.post,
            }.get(http_method, session.get)

            response = None
            if http_method == "POST" or http_method == "PUT":
                response = await method_func(url=params["url"], json=params["params"])
            else:
                session.headers.update(
                    {
                        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
                    }
                )
                response =  await method_func(url=params["url"])
            self.logger.debug("raw response from server:" + await response.text())
            await self._handle_rest_exception(response)
            try:
                data = await response.json()
            except ValueError:
                data = await response.text()
            result = data
            response.close()
            return result

    async def _handle_rest_exception(self, response):
        status_code = response.status
        if status_code <= 400:
            return
        if 400 < status_code < 500:
            try:
                err = await response.json()
            except JSONDecodeError:
                raise ClientError(
                    status_code, None, await response.text(), None, response.headers
                )
            error_data = None
            if "data" in err:
                error_data = err["data"]
            raise ClientError(
                status_code, err["code"], err["message"], response.headers, error_data
            )
        raise ServerError(status_code, await response.text())