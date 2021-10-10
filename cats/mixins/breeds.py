from ..utils import Breed, _resolve_query
from .base import BaseMixin
from urllib.parse import quote


class BreedsMixin(BaseMixin):
    def get_breeds(
        self, *, attach_breed: int = 0, page: int = None, limit: int = None
    ):
        p = _resolve_query(attach_breed=attach_breed, page=page, limit=limit)
        s = self.session.get(f"{self.BASE}/breeds", params=p)
        json = s.json()
        return [Breed(**data) for data in json]

    def search_breed(self, breed: str):
        url = f"{self.BASE}/breeds/search?q={quote(breed)}"
        res = self.session.get(url)
        json = res.json()
        return Breed(**json[0])
