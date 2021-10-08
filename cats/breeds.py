import requests
from .utils import Breed, BaseMixin
from urllib.parse import quote

class BreedsMixin(BaseMixin):

    def get_breeds(self):
        ses = self.session
        s = ses.get(f"{self.BASE}/breeds")
        json = s.json()
        return [Breed(**data) for data in json]

    def search_breed(self, breed: str):
        url = f"{self.BASE}/breeds/search?q={quote(breed)}"
        res = self.session.get(url)
        json = res.json()
        return Breed(**json[0])
