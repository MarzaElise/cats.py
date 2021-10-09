
from ._dataclasses import (
    Breed,
    Category,
    Vote,
    Response,
    Favourite,
    FavouriteImage,
    Image
)

def _resolve_query(**kwargs):
    query = {}
    for k, v in kwargs.items():
        if k is not None:
            query[k] = v
    return query

__all__ = (
    "Breed",
    "Category",
    "Vote",
    "Response",
    "Favourite",
    "FavouriteImage",
    "Image"
)
