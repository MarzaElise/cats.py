from ..utils import Breed, _resolve_query
from .base import BaseMixin
from urllib.parse import quote


class BreedsMixin(BaseMixin):
    async def get_breeds(
        self, *, attach_breed: int = 0, page: int = None, limit: int = None
    ):
        """
        Returns all the breeds available as a list of ``cats.Breed`` instance

        Arguments:
            ``attach_breed`` (int, optional): Defaults to 0.
            ``page`` (int, optional): For pagination. Defaults to None.
            ``limit`` (int, optional): Limit how many breeds should be returned. Defaults to None.

        Returns:
            ``List[cats.Breed]`` : All the breeds available
        """
        p = _resolve_query(attach_breed=attach_breed, page=page, limit=limit)
        s = await self.session.get(f"{self.BASE}/breeds", params=p)
        json = await s.json()
        return [Breed(**data) for data in json]

    async def search_breed(self, breed: str):
        """Search for a specific breed

        Arguments:
            ``breed`` (str): The breed to search for

        Returns:
            ``cats.Breed``: The breed object related to the breed you searched for
        """
        url = f"{self.BASE}/breeds/search?q={quote(breed)}"
        res = await self.session.get(url)
        json = await res.json()
        return Breed(**json[0])
