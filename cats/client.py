from cats.mixins.favourites import FavouritesMixin
from .mixins import *
import requests

class Client(
    BreedsMixin, 
    CategoriesMixin,
    VotesMixin,
    FavouritesMixin
):

    BASE = "https://api.thecatapi.com/v1"

    def __init__(self, api_key: str, *, session: requests.Session = None):
        self.session = session or requests.Session()
        self.api_key = api_key
        self.session.headers["x-api-key"] = self.api_key
