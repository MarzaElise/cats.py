import requests

class BaseMixin:
    api_key: str
    BASE: str
    session: requests.Session
