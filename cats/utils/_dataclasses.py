from pydantic import BaseModel
from typing import Optional, TypeAlias, Union

opt_str: TypeAlias = Optional[str]
opt_int: TypeAlias = Optional[int]


class Breed(BaseModel):

    id: opt_str
    name: opt_str
    temperament: opt_str
    life_span: opt_str
    alt_names: opt_str
    wikipedia_url: opt_str
    origin: opt_str
    weight_imperial: opt_str
    country_codes: opt_str
    country_code: opt_str
    description: opt_str
    weight: opt_str
    cfa_url: opt_str
    vetstreet_url: opt_str
    vcahospitals_url: opt_str
    reference_image_id: opt_str
    lap: opt_str
    image: opt_str

    experimental: opt_int
    suppressed_tail: opt_int
    indoor: opt_int
    hairless: opt_int
    natural: opt_int
    rare: opt_int
    rex: opt_int
    supress_tail: opt_int
    short_legs: opt_int
    hypoallergenic: opt_int
    adaptability: opt_int
    affection_level: opt_int
    child_friendly: opt_int
    dog_friendly: opt_int
    stranger_friendly: opt_int
    cat_friendly: opt_int
    energy_level: opt_int
    grooming: opt_int
    health_issues: opt_int
    intelligence: opt_int
    shedding_level: opt_int
    social_needs: opt_int
    vocalisation: opt_int
    bidability: opt_int


class Category(BaseModel):

    id: int
    name: str


class Vote(BaseModel):

    id: str
    image_id: str
    sub_id: opt_str
    created_at: str
    value: int
    country_code: opt_str
    user_id: opt_str


class Response(BaseModel):

    id: Union[str, int, None]
    message: str
    level: opt_str
    status: opt_int


class FavouriteImage(BaseModel):

    id: str
    url: str


class Favourite(BaseModel):

    id: str
    image_id: str
    sub_id: str
    created_at: str
    image: FavouriteImage
    user_id: str

    def __post_init__(self):
        self.image = FavouriteImage(**self.image)


class Image(BaseModel):

    id: str
    url: str
    width: int
    height: int
    created_at: str
    sub_id: str
    original_filename: str

    breeds: Breed
    categories: Category


class Analysis(BaseModel):

    image_id: str
    labels: list[dict]
    moderation_labels: list[dict]
    vendor: str
    approved: int
    rejected: int
