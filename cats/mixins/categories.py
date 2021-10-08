from ..utils import BaseMixin, Category


class CategoriesMixin(BaseMixin):

    def get_categories(self, *, limit: int = None, page: int = None):
        query = {}
        if limit is not None:
            query["limit"] = limit
        if page is not None:
            query["page"] = page
        url = f"{self.BASE}/categories"
        res = self.session.get(url, params=query)
        json = res.json()
        return [Category(**data) for data in json]
