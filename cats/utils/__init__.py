
from ._dataclasses import (
    Breed,
    Category,
    Vote,
    Response,
    Favourite,
    FavouriteImage,
    Image,
    Analysis
)
from .exceptions import *

def _resolve_query(**kwargs):
    query = {}
    for k, v in kwargs.items():
        if k is not None:
            query[k] = v
    return query

def _raise_for_status(status_code: int):
    if status_code == 404:
        raise NotFound(f"Requested URL was not found. Status code - {status_code}")
    if status_code == 403:
        raise Forbidden(f"Invalid API key. Status code - {status_code}")
    if status_code >= 500:
        raise ServerError(f"Unknown server side error. Status code - {status_code}")
    if str(status_code).startswith("2"):
        return True
    raise HTTPException(f"Unhandled status code exception - {status_code}")

__all__ = (
    "Breed",
    "Category",
    "Vote",
    "Response",
    "Favourite",
    "FavouriteImage",
    "Image",
    "Analysis",
    "NotFound",
    "Forbidden",
    "ServerError",
    "HTTPException"
)
