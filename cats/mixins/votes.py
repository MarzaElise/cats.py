from .base import BaseMixin
from ..utils import Vote, Response, _resolve_query


class VotesMixin(BaseMixin):
    def get_all_votes(
        self, sub_id: str = None, *, limit: int = None, page: int = None
    ):
        """Get all the votes that belong to your account

        Arguments:
            ``sub_id`` (str, optional): For filtering. Defaults to None.
            ``limit`` (int, optional): Limits the amount of responses returned. Defaults to None.
            ``page`` (int, optional): For pagination. Defaults to None.

        Returns:
            ``List[cats.Vote]``: All the votes that belong to your account filtered through limit and page kwargs
        """
        query = _resolve_query(sub_id=sub_id, limit=limit, page=page)
        url = self.BASE + "/votes"
        res = self.session.get(url, params=query)
        json = res.json()
        return [Vote(**data) for data in json]

    def vote_image(self, *, image_id: str, value: int, sub_id: str = None):
        """Upvote or Downvote an image

        Arguments:
            ``image_id`` (str): The ID of the image to vote
            ``sub_id`` (str, optional): Unique identification for you. Defaults to None
            ``value`` (int): 0 or 1 where 0 downvotes and 1 upvotes

        Returns:
            ``cats.Response``: Response returned by the API. may contain unsuccesful value
        """
        assert isinstance(value, int) and value in {
            0,
            1,
        }, "Value must be either 0 or 1"
        body = _resolve_query(image_id=image_id, sub_id=sub_id, value=value)
        url = f"{self.BASE}/votes"
        res = self.session.post(url, json=body)
        json = res.json()
        return Response(**json)

    def get_vote(self, vote_id: str):
        """Get a specific vote that belongs to you

        Arguments:
            ``vote_id`` (str): ID of the vote. Returnede with the reponse when calling ``Client.vote_image``

        Returns:
            ``cats.Vote``: If the request was succesful, information about the vote is returned
            ``cats.Response``: Request was not succesful.
        """
        url = f"{self.BASE}/votes/{vote_id}"
        res = self.session.get(url)
        json = res.json()
        if res.status_code == 200:
            return Vote(**json)
        return Response(**json)

    def delete_vote(self, vote_id: str):
        """Delete a vote that belongs to you

        Args:
            ``vote_id`` (str): ID of the vote you are trying to delete

        Returns:
            ``cats.Response``: Response returned by the API. may contain unsuccesful value
        """
        url = f"{self.BASE}/votes/{vote_id}"
        res = self.session.delete(url)
        json = res.json()
        return Response(**json)
