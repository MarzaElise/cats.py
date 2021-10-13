from .base import BaseMixin
from ..utils import Favourite, Response, _resolve_query


class FavouritesMixin(BaseMixin):
    def get_all_favourites(
        self, *, sub_id: str = None, limit: str = None, page: str = None
    ):
        """Get all of the favourites that belong to your account

        Arguments:
            ``sub_id`` (str, optional): For filtering. Defaults to None.
            ``limit`` (str, optional): limit the amount of results. Defaults to None.
            ``page`` (str, optional): For pagination. Defaults to None.

        Returns:
            ``List[cats.Favourite]``: Favourites belonging to your account
        """
        url = f"{self.BASE}/favourites"
        query = _resolve_query(sub_id=sub_id, limit=limit, page=page)
        res = self.session.get(url, params=query)
        json = res.json()
        return [Favourite(**data) for data in json]

    def save_favourite(self, image_id: str, sub_id: str = None):
        """Save an image as favourite

        Arguments:
            ``image_id`` (str): The id of the image to save as favourite
            ``sub_id`` (str, optional): Defaults to None.

        Returns:
            ``cats.Response``: Response returned by the API, may contain unsuccesful response too
        """
        body = _resolve_query(image_id=image_id, sub_id=sub_id)
        url = f"{self.BASE}/favourites"
        res = self.session.post(url, json=body)
        json = res.json()
        return Response(**json)

    def get_favourite(self, favourite_id: str):
        """Get a specific favourite belonging to your account

        Arguments:
            ``favourite_id`` (str): ID of the favourite object. Return with the response when using ``cats.Client.save_favourite``

        Returns:
            ``cats.Favourite``: Information about the favourite returned by the API itself
        """
        url = f"{self.BASE}/favourites/{favourite_id}"
        res = self.session.get(url)
        json = res.json()
        return Favourite(**json)

    def delete_favourite(self, favourite_id: str):
        """Delete an image from your favourites

        Arguments:
            ``favourite_id`` (str): ID of the favourite object. Return with the response when using ``cats.Client.save_favourite``

        Returns:
            ``cats.Response``: Response returned by the API, may contain unsuccesful response too
        """
        url = f"{self.BASE}/favourites/{favourite_id}"
        res = self.session.delete(url)
        json = res.json()
        return Response(**json)
