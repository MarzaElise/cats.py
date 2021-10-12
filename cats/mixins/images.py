from .base import BaseMixin
from ..utils import _resolve_query, Image, Response, Analysis
import base64
import io


class ImagesMixin(BaseMixin):
    def get_all_images(
        self,
        *,
        size: str = None,
        mime_types: list[str] = None,
        order: str = None,
        limit: int = None,
        page: int = None,
        category_ids: list[int] = None,
        format: str = None,
        breed_id: str = None,
    ):
        assert size.lower() in {"small", "thumb", "med", "full"}, "size must be one of small, thumb, med, full"
        assert order.upper() in {"RANDOM", "ASC", "DESC"}, "order should be one of RANDOM, ASC, DESC"
        assert limit >= 1 and limit < 100, "limit cannot be below 1 or above 100"
        assert page >= 0, "page must be higher than or equal 0"
        assert format.lower() in {"json", "src"}, "format must be one of json, src"

        query = _resolve_query(
            size=size.lower(),
            mime_types=list(set(mime_types)), # only unique items allowed
            order=order.upper(),
            limit=limit,
            page=page,
            category_ids=list(set(category_ids)),
            format=format,
            breed_id=breed_id,
        )
        url = f"{self.BASE}/images/search"
        res = self.session.get(url, params=query)
        json = res.json()
        return [Image(**data) for data in json]

    def get_own_image(self, **kwargs):  # needs a better name
        # Note:
        # see https://docs.thecatapi.com/api-reference/images/images-get-uploads
        # for valid kwargs

        limit=kwargs.get("limit", None)
        page=kwargs.get("page", None)
        order=kwargs.get("order", None)
        sub_id=kwargs.get("sub_id", None)
        breed_ids=kwargs.get("breed_ids", None)
        category_ids=kwargs.get("category_ids", None)
        original_filename=kwargs.get("original_filename", None)
        format=kwargs.get("format", None)
        include_vote=kwargs.get("include_vote", None)
        include_favourite=kwargs.get("include_favourite", None)

        assert limit >= 1 and limit < 100, "limit cannot be below 1 or above 100"
        assert page >= 1, "page must be higher than or equal 1"
        assert order.upper() in {"RANDOM", "ASC", "DESC"}, "order should be one of RANDOM, ASC, DESC"
        assert len(sub_id) >= 0 and len(sub_id) < 255, "length of sub_id must be higher than 0 and lower than 255"
        category_ids=list(set(category_ids))
        breed_ids=list(set(breed_ids))
        assert len(original_filename) >= 0 and len(original_filename) < 100, "Length of original filename cannot be above 100 or below 0"
        assert format.lower() in {"json", "src"}, "format must be one of json, src"
        assert include_favourite in {1, 0}, "include_favourite must be one of 1, 0"
        assert include_vote in {1, 0}, "include_vote must be one of 1, 0"

        url = f"{self.BASE}/images"
        query = _resolve_query(
            limit=limit,
            page=page,
            order=order,
            sub_id=sub_id,
            breed_ids=breed_ids,
            category_ids=category_ids,
            original_filename=original_filename,
            format=format,
            include_vote=include_vote,
            include_favourite=include_favourite,
        )
        res = self.session.get(url, params=query)
        json = res.json()
        return [Image(**data) for data in json]

    def upload_image(self, file_name: str):
        raise NotImplementedError("This function will be implemented soon")

    #     url = f"{self.BASE}/images/upload"
    #     with open(file_name, "rb") as file:
    #         res = self.session.post(url, files={"file": file})
    #     return res.text

    def get_image(self, image_id: str):
        url = f"{self.BASE}/images/{image_id}"
        res = self.session.get(url)
        json = res.json()
        return Image(**json)

    def delete_image(self, image_id: str):
        url = f"{self.BASE}/images/{image_id}"
        res = self.session.delete(url)
        json = res.json()
        return Response(**json)

    def get_image_analysis(self, image_id: str):
        url = f"{self.BASE}/images/{image_id}/analysis"
        res = self.session.get(url)
        json = res.json()
        return [Analysis(**data) for data in json]

    def search_image(
        self, *, breed_ids: str = None, category_ids: list[int] = None
    ):
        url = f"{self.BASE}/images/search"
        query = _resolve_query(breed_ids=breed_ids, category_ids=category_ids)
        res = self.session.get(url, params=query)
        json = res.json()
        return [Image(**data) for data in json]
