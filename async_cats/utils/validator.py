from pydantic import BaseModel, validator
from typing import Optional, List


class ValidateArguments(BaseModel):

    limit: int = None
    page: int = None
    order: str = None
    sub_id: str = None
    size: str = None
    original_filename: str = None
    format: str = None
    include_vote: int = None
    mime_types: List[str] = None
    include_favourite: Optional[int] = None

    @validator("mime_types")
    def validate_mime_types(cls, mime_types: List[str]):
        if mime_types is None:
            return mime_types
        for type_ in mime_types:
            if type_.lower() not in {"jpg", "png", "gif"}:
                raise ValueError(
                    "Expected jpg, png or gif. Received {} instead".format(
                        type_.lower()
                    )
                )
        return mime_types

    @validator("size")
    def validate_size(cls, size: str):
        if size is None:
            return size
        if size and size.lower() not in {"small", "med", "full", "thumb"}:
            raise ValueError("size must be one of small, med, full, thumb")
        return size

    @validator("include_favourite")
    def validate_favourite(cls, item: int):
        if item in {0, 1, None}:
            return item
        raise ValueError("include_favourite must be either 0, 1 or None")

    @validator("include_vote")
    def validate_vote(cls, item: int):
        if item in {0, 1, None}:
            return item
        raise ValueError("include_vote must be either 0, 1 or None")

    @validator("limit")
    def validate_limit(cls, limit: int):
        if limit is None:
            return limit  # early return
        if limit > 100:
            raise ValueError("limit must be below 100")
        if limit < 1:
            raise ValueError("limit should be higher than")
        return limit

    @validator("page")
    def validate_page(cls, item: int):
        if item is None:
            return item
        if item < 1:
            raise ValueError("page must be higher than or equal to 1")
        return item

    @validator("order")
    def validate_order(cls, order: str):
        if order is None:
            return order
        valid = {"RANDOM", "ASC", "DESC"}
        if order and order.upper() not in valid:
            raise ValueError("order must be one of RANDOM, ASC, DESC")
        return order.upper()

    @validator("sub_id")
    def validate_sub_id(cls, sub_id: str):
        if sub_id:
            if len(sub_id) < 0:
                raise ValueError("length of sub_id must be higher than 0")
            if len(sub_id) > 255:
                raise ValueError("length of sub_id must be lower than 255")
        return sub_id

    @validator("format")
    def validate_format(cls, format: str):
        if format is None:
            return format
        if format and format.lower() in {"json", "src"}:
            return format.lower()
        raise ValueError("format must be either json or src")
