from pydantic import BaseModel, Field

from app.elastic.handler.data_handler import get_json_format


class Location(BaseModel):
    lat: float
    lon: float


class Pin(BaseModel):
    location: Location


class MichelinRestaurant(BaseModel):
    name: str
    year: int
    pin: Pin
    city: str
    region: str
    zipCode: str
    cuisine: str
    price: str
    url: str
    star: int


class DocumentIndex(BaseModel):
    id: str = Field(alias="_id", default=None)
    index: str = "michelin_restaurants"
    document: MichelinRestaurant


if __name__ == "__main__":
    data = get_json_format()
    model = MichelinRestaurant(**data[0])
    print(model)
    doc = DocumentIndex(document=model)
