from dataclasses import dataclass
from typing import Optional, TypeAlias, Union

opt_str: TypeAlias = Optional[str]
opt_int: TypeAlias = Optional[int]

@dataclass()
class Breed:

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


@dataclass
class Category:

    id: int
    name: str

@dataclass
class Vote:

    id: str
    image_id: str
    sub_id: opt_str
    created_at: str
    value: int
    country_code: opt_str = None
    user_id: opt_str = None

@dataclass
class VoteResponse:

    id: Union[str, int, None] = None
    message: str = None
    level: opt_str = None
    status: opt_int = None
