from .base import BaseMixin
from ..utils import Vote, VoteResponse

class VotesMixin(BaseMixin):

    def get_votes(self, sub_id: str = None, *, limit: int = None, page: int = None):
        query = {}
        if sub_id is not None:
            query["sub_id"] = sub_id
        if limit is not None:
            query["limit"] = limit
        if page is not None:
            query["page"] = page
        url = self.BASE + "/votes"
        res = self.session.get(url, params=query)
        json = res.json()
        return [Vote(**data) for data in json]

    def vote_image(self, *, image_id: str, sub_id: str, value: int):
        body = { # request body
            "image_id": image_id,
            "sub_id": sub_id,
            "value": value
        }
        url = f"{self.BASE}/votes"
        res = self.session.post(url, json=body)
        json = res.json()
        return VoteResponse(**json)
