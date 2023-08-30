from pydantic import BaseModel, Field

from app.elastic.load.models import Location


class MatchMichelinOptions(BaseModel):
    """Model for match query.

    Does not include all fields from MichelinRestaurant model.
    """
    name: str = None
    year: int = None
    city: str = None
    region: str = None
    zipCode: str = None
    cuisine: str = None
    price: str = None
    url: str = None
    star: int = None


class Match(BaseModel):
    match: MatchMichelinOptions


class GeoDistance(BaseModel):
    """Model for geo distance query.

    Overrides dict method to return a dict with the correct format
    (using field alias that implements dot notation).
    In case we do not want to use 'by_alias' somewhere else.
    """
    distance: str
    document_pin_location: Location = Field(alias="pin.location")

    def dict(self, *, exclude_none: bool = False, **kwargs) -> 'DictStrAny':
        return dict(
            self._iter(
                to_dict=True, by_alias=True, exclude_none=exclude_none,
            )
        )


class Filter(BaseModel):
    geo_distance: GeoDistance


class Bool(BaseModel):
    must: list[Match] = None
    filter: Filter = None


class Query(BaseModel):
    """Model for match query."""
    bool: Bool = None
    match: MatchMichelinOptions = None
    match_all: dict = None


class Search(BaseModel):
    """Model for search query."""
    index: str
    query: Query
    size: int = 1000
