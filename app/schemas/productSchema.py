from decimal import Decimal
from typing import Optional
import uuid
from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    sku: str = Field(..., min_length=1, max_length=100)
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=500)
    unit_price: Decimal = Field(..., gt=0, decimal_places=2)
    amount_in_stock: int = Field(default=0, ge=0)


class ProductCreate(ProductBase):

    pass


class ProductRead(ProductBase):

    id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)
