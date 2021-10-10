from requests import Session, Response
from .utils import _raise_for_status



class HTTPClient(Session):

    def __init__(self, api_key) -> None:
        super().__init__()
        self.headers["x-api-key"] = api_key

    def post(self, url, data=None, json=None, **kwargs) -> Response:
        res = super().post(url, data=data, json=json, **kwargs)
        s = _raise_for_status(res.status_code)
        if s:
            return res

    def get(self, url, **kwargs) -> Response:
        res = super().get(url, **kwargs)
        s = _raise_for_status(res.status_code)
        if s:
            return res

    def delete(self, url, **kwargs) -> Response:
        res = super().delete(url, **kwargs)
        s = _raise_for_status(res.status_code)
        if s:
            return res
