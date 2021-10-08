from .breeds import BreedsMixin
import requests

class Client(BreedsMixin):

    BASE = "https://api.thecatapi.com"

    def __init__(self, api_key: str, *, session: requests.Session = None):
        self.session = session or requests.Session()
        self.api_key = api_key
