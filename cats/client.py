from .mixins import *
import requests
from .http import HTTPClient

class Client(
    BreedsMixin, 
    CategoriesMixin,
    VotesMixin,
    FavouritesMixin,
    ImagesMixin
):

    BASE = "https://api.thecatapi.com/v1"

    def __init__(self, api_key: str):
        self.session = HTTPClient(api_key)
        self.api_key = api_key
        self.session.headers["x-api-key"] = self.api_key
