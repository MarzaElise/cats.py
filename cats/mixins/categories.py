from ..utils import Category, _resolve_query
from .base import BaseMixin


class CategoriesMixin(BaseMixin):
    def get_categories(self, *, limit: int = None, page: int = None):
        query = _resolve_query(limit=limit, page=page)
        url = f"{self.BASE}/categories"
        res = self.session.get(url, params=query)
        json = res.json()
        return [Category(**data) for data in json]
