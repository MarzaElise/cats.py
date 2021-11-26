from aiohttp import ClientSession, ClientResponse
from .utils import _raise_for_status


class HTTPClient(ClientSession):
    def __init__(self, api_key) -> None:
        super().__init__()
        self.headers["x-api-key"] = api_key

    async def post(
        self, url, data=None, json=None, **kwargs
    ) -> ClientResponse:
        res = await super().post(url, data=data, json=json, **kwargs)
        s = _raise_for_status(res.status)
        if s:
            return res

    async def get(self, url, **kwargs) -> ClientResponse:
        res = await super().get(url, **kwargs)
        s = _raise_for_status(res.status)
        if s:
            return res

    async def delete(self, url, **kwargs) -> ClientResponse:
        res = await super().delete(url, **kwargs)
        s = _raise_for_status(res.status)
        if s:
            return res
