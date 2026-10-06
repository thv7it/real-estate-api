from enum import Enum


class PropertyType(str, Enum):
    APARTMENT = "apartment"
    HOUSE = "house"
    LAND = "land"
    COMMERCIAL = "commercial"


class DealType(str, Enum):
    SALE = "sale"
    RENT = "rent"