from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field
from app.enums import PropertyType, DealType


class PropertyCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str | None = None
    price: Decimal = Field(gt=0)
    city: str = Field(min_length=2, max_length=100)
    address: str = Field(min_length=3, max_length=255)
    rooms: int | None = Field(default=None, gt=0)
    area: Decimal = Field(gt=0)
    property_type: PropertyType
    deal_type: DealType

class PropertyUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=200)
    description: str | None = None
    price: Decimal | None = Field(default=None, gt=0)
    city: str | None = Field(default=None, min_length=2, max_length=100)
    address: str | None = Field(default=None, min_length=3, max_length=255)
    rooms: int | None = Field(default=None, gt=0)
    area: Decimal | None = Field(default=None, gt=0)
    property_type: PropertyType | None = None
    deal_type: DealType | None = None
    is_active: bool | None = None
    

class PropertyResponse(BaseModel):
    id: int
    title: str
    description: str | None
    price: Decimal
    city: str
    address: str
    rooms: int | None
    area: Decimal
    property_type: str
    deal_type: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)