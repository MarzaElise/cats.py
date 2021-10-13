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
        """Get all of the public images

        Arguments:
            ``size`` (str, optional): Size of each image, must be on of `small`, `thumb`, `med`, `full`. Defaults to None.
            ``mime_types`` (list[str], optional): See the API [documentation](https://docs.thecatapi.com). Defaults to None.
            ``order`` (str, optional): The order the images should be sorted in, must be one of `RANDOM` `ASC` `DESC`. Defaults to None.
            ``limit`` (int, optional): Limits the amount of results. Defaults to None.
            ``page`` (int, optional): For pagination. Defaults to None.
            ``category_ids`` (list[int], optional): Filters images and returns only the images that belong to the relevant categories. Defaults to None.
            ``format`` (str, optional): must be one of `json` `src`. Defaults to None.
            ``breed_id`` (str, optional): Filters images for this breed. Defaults to None.

        Returns:
            ``List[cats.Image]`` : Images returned by the API with the given filters
        """
        assert size.lower() in {
            "small",
            "thumb",
            "med",
            "full",
        }, "size must be one of small, thumb, med, full"
        assert order.upper() in {
            "RANDOM",
            "ASC",
            "DESC",
        }, "order should be one of RANDOM, ASC, DESC"
        assert (
            limit >= 1 and limit < 100
        ), "limit cannot be below 1 or above 100"
        assert page >= 0, "page must be higher than or equal 0"
        assert format.lower() in {
            "json",
            "src",
        }, "format must be one of json, src"

        query = _resolve_query(
            size=size.lower(),
            mime_types=list(set(mime_types)),  # only unique items allowed
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
        """Get an image uploaded by you

        Arguments:
            ``kwargs`` (dict, optional): for filtering the response and the request. See the API [documentation](https://docs.thecatapi.com) for more details

        Returns:
            ``List[cats.Image]`` : All the images filtered by the kwargs
        """

        # Note:
        # see https://docs.thecatapi.com/api-reference/images/images-get-uploads
        # for valid kwargs

        limit = kwargs.get("limit", None)
        page = kwargs.get("page", None)
        order = kwargs.get("order", None)
        sub_id = kwargs.get("sub_id", None)
        breed_ids = kwargs.get("breed_ids", None)
        category_ids = kwargs.get("category_ids", None)
        original_filename = kwargs.get("original_filename", None)
        format = kwargs.get("format", None)
        include_vote = kwargs.get("include_vote", None)
        include_favourite = kwargs.get("include_favourite", None)

        assert (
            limit >= 1 and limit < 100
        ), "limit cannot be below 1 or above 100"
        assert page >= 1, "page must be higher than or equal 1"
        assert order.upper() in {
            "RANDOM",
            "ASC",
            "DESC",
        }, "order should be one of RANDOM, ASC, DESC"
        assert (
            len(sub_id) >= 0 and len(sub_id) < 255
        ), "length of sub_id must be higher than 0 and lower than 255"
        category_ids = list(set(category_ids))
        breed_ids = list(set(breed_ids))
        assert (
            len(original_filename) >= 0 and len(original_filename) < 100
        ), "Length of original filename cannot be above 100 or below 0"
        assert format.lower() in {
            "json",
            "src",
        }, "format must be one of json, src"
        assert include_favourite in {
            1,
            0,
        }, "include_favourite must be one of 1, 0"
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
        """Not implemented yet.

        Arguments:
            ``file_name`` (str): File name to use while uploading

        Raises:
            ``NotImplementedError`` : method not implemented
        """
        raise NotImplementedError("This function will be implemented soon")

    #     url = f"{self.BASE}/images/upload"
    #     with open(file_name, "rb") as file:
    #         res = self.session.post(url, files={"file": file})
    #     return res.text

    def get_image(self, image_id: str):
        """
        Get the image matching the image_id provided

        Note: Some attributes will be ``None`` if you dont own the image

        Arguments:
            ``image_id`` (str): The image id to re

        Returns:
            ``cats.Image`` : The image you requested
        """
        url = f"{self.BASE}/images/{image_id}"
        res = self.session.get(url)
        json = res.json()
        return Image(**json)

    def delete_image(self, image_id: str):
        """Deletr an image posted by you

        Arguments:
            ``image_id`` (str): The ID of the image to delete

        Returns:
            ``cats.Response``: Response returned by the API. May contain unsuccesful values
        """
        url = f"{self.BASE}/images/{image_id}"
        res = self.session.delete(url)
        json = res.json()
        return Response(**json)

    def get_image_analysis(self, image_id: str):
        """
        Get the Analysis performed on the Image during upload.

        Arguments:
            ``image_id`` (str): The image's id to get the Analysis of

        Returns:
            ``cats.Analysis``: The analysis of the image you requested
        """
        url = f"{self.BASE}/images/{image_id}/analysis"
        res = self.session.get(url)
        json = res.json()
        return [Analysis(**data) for data in json]

    def search_image(
        self, *, breed_ids: str = None, category_ids: list[int] = None
    ):
        """Search for an image

        Arguments:
            ``breed_ids`` (str, optional): Filter the images and receive only this specific breed. Defaults to None.
            ``category_ids`` (list[int], optional): Returns only images that belong to this category. Defaults to None.

        Returns:
            ``List[cats.Image]``: List of images that match your filters
        """
        url = f"{self.BASE}/images/search"
        query = _resolve_query(breed_ids=breed_ids, category_ids=category_ids)
        res = self.session.get(url, params=query)
        json = res.json()
        return [Image(**data) for data in json]
