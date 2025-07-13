from typing import Optional
import uuid
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    full_name: str = Field(..., min_length=1, max_length=255, description="User's full name")
    is_active: bool = Field(default=True, description="User's status")


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="User's password")


class UserRead(UserBase):
    id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = Field(None, description="User's email address")
    full_name: Optional[str] = Field(None, min_length=1, max_length=255, description="User's full name")
    password: Optional[str] = Field(None, min_length=8, description="User's new password")
    is_active: Optional[bool] = Field(None, description="User's status")

    model_config = ConfigDict(from_attributes=True)