from .base import BaseMixin
from ..utils import Favourite, Response, _resolve_query


class FavouritesMixin(BaseMixin):
    def get_all_favourites(
        self, *, sub_id: str = None, limit: str = None, page: str = None
    ):
        url = f"{self.BASE}/favourites"
        query = _resolve_query(sub_id=sub_id, limit=limit, page=page)
        res = self.session.get(url, params=query)
        json = res.json()
        return [Favourite(**data) for data in json]

    def save_favourite(self, image_id: str, sub_id: str = None):
        body = _resolve_query(image_id=image_id, sub_id=sub_id)
        url = f"{self.BASE}/favourites"
        res = self.session.post(url, json=body)
        json = res.json()
        return Response(**json)

    def get_favourite(self, favourite_id: str):
        url = f"{self.BASE}/favourites/{favourite_id}"
        res = self.session.get(url)
        json = res.json()
        return Favourite(**json)

    def delete_favourite(self, favourite_id: str):
        url = f"{self.BASE}/favourites/{favourite_id}"
        res = self.session.delete(url)
        json = res.json()
        return Response(**json)
