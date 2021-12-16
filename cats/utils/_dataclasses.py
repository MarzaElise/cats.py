from pydantic import BaseModel
from typing import Any, Optional, TypeAlias, Union


class Breed(BaseModel):

    id: Optional[Union[str, Any]]
    name: Optional[Union[str, Any]]
    temperament: Optional[Union[str, Any]]
    life_span: Optional[Union[str, Any]]
    alt_names: Optional[Union[str, Any]]
    wikipedia_url: Optional[Union[str, Any]]
    origin: Optional[Union[str, Any]]
    weight_imperial: Optional[Union[str, Any]]
    country_codes: Optional[Union[str, Any]]
    country_code: Optional[Union[str, Any]]
    description: Optional[Union[str, Any]]
    weight: Optional[Union[str, Any]]
    cfa_url: Optional[Union[str, Any]]
    vetstreet_url: Optional[Union[str, Any]]
    vcahospitals_url: Optional[Union[str, Any]]
    reference_image_id: Optional[Union[str, Any]]
    lap: Optional[Union[str, Any]]
    image: Optional[Union[str, Any]]

    experimental: Optional[Union[int, Any]]
    suppressed_tail: Optional[Union[int, Any]]
    indoor: Optional[Union[int, Any]]
    hairless: Optional[Union[int, Any]]
    natural: Optional[Union[int, Any]]
    rare: Optional[Union[int, Any]]
    rex: Optional[Union[int, Any]]
    supress_tail: Optional[Union[int, Any]]
    short_legs: Optional[Union[int, Any]]
    hypoallergenic: Optional[Union[int, Any]]
    adaptability: Optional[Union[int, Any]]
    affection_level: Optional[Union[int, Any]]
    child_friendly: Optional[Union[int, Any]]
    dog_friendly: Optional[Union[int, Any]]
    stranger_friendly: Optional[Union[int, Any]]
    cat_friendly: Optional[Union[int, Any]]
    energy_level: Optional[Union[int, Any]]
    grooming: Optional[Union[int, Any]]
    health_issues: Optional[Union[int, Any]]
    intelligence: Optional[Union[int, Any]]
    shedding_level: Optional[Union[int, Any]]
    social_needs: Optional[Union[int, Any]]
    vocalisation: Optional[Union[int, Any]]
    bidability: Optional[Union[int, Any]]


class Category(BaseModel):

    id: Union[int, Any]
    name: Union[str, Any]


class Vote(BaseModel):

    id: Union[str, Any]
    image_id: Union[str, Any]
    sub_id: Optional[Union[str, Any]]
    created_at: Union[str, Any]
    value: Union[int, Any]
    country_code: Optional[Union[str, Any]]
    user_id: Optional[Union[str, Any]]


class Response(BaseModel):

    id: Union[str, int, None]
    message: Union[str, Any]
    level: Optional[Union[str, Any]]
    status: Optional[Union[int, Any]]


class FavouriteImage(BaseModel):

    id: Union[str, Any]
    url: Union[str, Any]


class Favourite(BaseModel):

    id: Union[str, Any]
    image_id: Union[str, Any]
    sub_id: Union[str, Any]
    created_at: Union[str, Any]
    image: FavouriteImage
    user_id: Union[str, Any]

    def __post_init__(self):
        self.image = FavouriteImage(**self.image)


class Image(BaseModel):

    id: Union[str, Any]
    url: Union[str, Any]
    width: Union[int, Any]
    height: Union[int, Any]
    created_at: Union[str, Any]
    sub_id: Union[str, Any]
    original_filename: Union[str, Any]

    breeds: Breed
    categories: Category



class Analysis(BaseModel):

    image_id: Union[str, Any]
    labels: list[dict]
    moderation_labels: list[dict]
    vendor: Union[str, Any]
    approved: Union[int, Any]
    rejected: Union[int, Any]
