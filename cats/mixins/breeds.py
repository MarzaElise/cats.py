from ..utils import Breed
from .base import BaseMixin
from urllib.parse import quote


class BreedsMixin(BaseMixin):
    def get_breeds(
        self, *, attach_breed: int = 0, page: int = None, limit: int = None
    ):
        p = {
            "attach_breed": attach_breed,
        }
        if page is not None:
            p["page"] = page
        if limit is not None:
            p["limit"] = limit

        s = self.session.get(f"{self.BASE}/breeds", params=p)
        json = s.json()
        return [Breed(**data) for data in json]

    def search_breed(self, breed: str):
        url = f"{self.BASE}/breeds/search?q={quote(breed)}"
        res = self.session.get(url)
        json = res.json()
        return Breed(**json[0])
