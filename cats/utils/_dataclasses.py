from pydantic import BaseModel
from typing import Optional, TypeAlias, Union

opt_str: TypeAlias = Optional[str]
opt_int: TypeAlias = Optional[int]


class Breed(BaseModel):

    id: opt_str = None
    name: opt_str = None
    temperament: opt_str = None
    life_span: opt_str = None
    alt_names: opt_str = None
    wikipedia_url: opt_str = None
    origin: opt_str = None
    weight_imperial: opt_str = None
    country_codes: opt_str = None
    country_code: opt_str = None
    description: opt_str = None
    weight: opt_str = None
    cfa_url: opt_str = None
    vetstreet_url: opt_str = None
    vcahospitals_url: opt_str = None
    reference_image_id: opt_str = None
    lap: opt_str = None
    image: opt_str = None

    experimental: opt_int = None
    suppressed_tail: opt_int = None
    indoor: opt_int = None
    hairless: opt_int = None
    natural: opt_int = None
    rare: opt_int = None
    rex: opt_int = None
    supress_tail: opt_int = None
    short_legs: opt_int = None
    hypoallergenic: opt_int = None
    adaptability: opt_int = None
    affection_level: opt_int = None
    child_friendly: opt_int = None
    dog_friendly: opt_int = None
    stranger_friendly: opt_int = None
    cat_friendly: opt_int = None
    energy_level: opt_int = None
    grooming: opt_int = None
    health_issues: opt_int = None
    intelligence: opt_int = None
    shedding_level: opt_int = None
    social_needs: opt_int = None
    vocalisation: opt_int = None
    bidability: opt_int = None


class Category(BaseModel):

    id: int = None
    name: str = None


class Vote(BaseModel):

    id: str
    image_id: str
    sub_id: opt_str
    created_at: str
    value: int
    country_code: opt_str = None
    user_id: opt_str = None


class Response(BaseModel):

    id: Union[str, int, None] = None
    message: str = None
    level: opt_str = None
    status: opt_int = None


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

    id: str = None
    url: str = None
    width: int = None
    height: int = None
    created_at: str = None
    sub_id: str = None
    original_filename: str = None

    breeds: Breed = None
    categories: Category = None

    def __post_init__(self):
        if self.categories is None:
            self.categories = []
        if self.breeds is None:
            self.breeds = []
        self.breeds = [
            Breed(**data) for data in self.breeds
        ]  # api returns a list
        self.categories = [
            Category(**data) for data in self.categories
        ]  # api returns list


class Analysis(BaseModel):

    image_id: str = None
    labels: list[dict] = None
    moderation_labels: list[dict] = None
    vendor: str = None
    approved: int = None
    rejected: int = None
