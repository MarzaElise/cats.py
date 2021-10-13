from ..utils import Category, _resolve_query
from .base import BaseMixin


class CategoriesMixin(BaseMixin):
    def get_categories(self, *, limit: int = None, page: int = None):
        """Get all the categories available

        Arguments:
            ``limit`` (int, optional): Limit the amount of results to be returned. Defaults to None.
            ``page`` (int, optional): For pagination. Defaults to None.

        Returns:
            ``List[cats.Category`` : A list of all the categories available
        """
        query = _resolve_query(limit=limit, page=page)
        url = f"{self.BASE}/categories"
        res = self.session.get(url, params=query)
        json = res.json()
        return [Category(**data) for data in json]
