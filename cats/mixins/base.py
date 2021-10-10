from ..http import HTTPClient

class BaseMixin:
    api_key: str
    BASE: str
    session: HTTPClient
