from .mixins import *
from .utils.constants import API_BASE_URL
import requests
from .http import HTTPClient


class Client(
    BreedsMixin, CategoriesMixin, VotesMixin, FavouritesMixin, ImagesMixin
):

    BASE = API_BASE_URL

    def __init__(self, api_key: str):
        self.session = HTTPClient(api_key)
        self.api_key = api_key
