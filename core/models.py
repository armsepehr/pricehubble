
from enum import Enum
from dataclasses import dataclass
from datetime import date

@dataclass
class PropertyType(Enum):
    apartment = "apartment"
    house = "house"

@dataclass
class Property:
    def __post_init__(self):
        if not (10<self.living_area<500):
            raise ValueError("living area should be between 10 and 500.")
        if not self.id:
            raise ValueError("id is not nullable")
        if not self.price:
            raise ValueError("price is not nullable")
        if not self.living_area:
            raise ValueError("living_area is not nullable")
        if not self.scraping_date:
            raise ValueError("scraping_date is not nullable")
        if not self.property_type:
            raise ValueError("property_type is not nullable")

    id: str
    price: float
    living_area: float 
    property_type: PropertyType 
    scraping_date: date

class ScrapedProperty:
    id: str
    raw_price: str
    property_type: str
    municipality: str
    scraping_date: str
