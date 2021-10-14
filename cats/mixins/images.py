from .base import BaseMixin
from ..utils import _resolve_query, Image, Response, Analysis, ValidateArguments
from typing import List, Optional


class ImagesMixin(BaseMixin):
    def get_all_images(
        self,
        *,
        size: str = None,
        mime_types: List[str] = None,
        order: str = None,
        limit: int = None,
        page: int = None,
        category_ids: List[int] = None,
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

        ValidateArguments(
            size=size,
            order=order,
            limit=limit,
            mime_types=mime_types,
            page=page,
            format=format
        )

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

    def get_own_image(  # needs a better name
        self,
        *,
        limit: int = None,
        page: int = None,
        order: str = None,
        sub_id: str = None,
        breed_ids: List[str] = None,
        category_ids: List[str] = None,
        original_filename: str = None,
        format: str = None,
        include_vote: int = None,
        include_favourite: Optional[int] = None
    ):
        """Get all the images uploaded by you

        Arguments:
            ``limit`` (int, optional): Limits the amount of results to be returned. Defaults to None.
            ``page`` (int, optional): For pagination. Defaults to None.
            ``order`` (str, optional): To sort the results, must be one of RANDOM, ASC, DESC. Defaults to None.
            ``sub_id`` (str, optional): For unique identification. Defaults to None.
            ``breed_ids`` (List[str], optional): unique list of breed ids for filtering. Defaults to None.
            ``category_ids`` (List[str], optional): unique list of category ids to filter the response. Defaults to None.
            ``original_filename`` (str, optional): To search for a match. Defaults to None.
            ``format`` (str, optional): format of the image. must be one of json or src. Defaults to None.
            ``include_vote`` (int, optional): See API [docs](https://docs.thecatapi.com). Defaults to None.
            ``include_favourite`` (Optional[int], optional): See API [docs](https://docs.thecatapi.com).. Defaults to None.

        Returns:
            ``List[cats.Image]``: All the images that belong to you
        """

        ValidateArguments(
            limit = limit,
            page = page,
            order = order,
            sub_id = sub_id,
            breed_ids = breed_ids,
            category_ids = category_ids,
            original_filename = original_filename,
            format = format,
            include_vote = include_vote,
            include_favourite = include_favourite
        ) # i dont need the return value, just need to validate them

        category_ids = list(set(category_ids))
        breed_ids = list(set(breed_ids))

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
