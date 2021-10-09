from .base import BaseMixin
from ..utils import _resolve_query, Image, Response
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
        breed_id: str = None
    ):
        # query = {}
        query = _resolve_query(
            size=size,
            mime_types=mime_types,
            order=order,
            limit=limit,
            page=page,
            category_ids=category_ids,
            format=format,
            breed_id=breed_id
        )
        url = f"{self.BASE}/images/search"
        res = self.session.get(url, params=query)
        json = res.json()
        return [Image(**data) for data in json]

    def get_own_image(self, **kwargs): # needs a better name
        # Note: 
        # see https://docs.thecatapi.com/api-reference/images/images-get-uploads 
        # for valid kwargs
        url = f"{self.BASE}/images"
        query = _resolve_query(
            limit=kwargs.get("limit", None),
            page=kwargs.get("page", None),
            order=kwargs.get("order", None),
            sub_id=kwargs.get("sub_id", None),
            breed_ids=kwargs.get("breed_ids", None),
            category_ids=kwargs.get("category_ids", None),
            original_filename=kwargs.get("original_filename", None),
            format=kwargs.get("format", None),
            include_vote=kwargs.get("include_vote", None),
            include_favourite=kwargs.get("include_favourite", None),
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

    def get_analysis(self, image_id: str):
        url = f"{self.BASE}/images/{image_id}/analysis"
