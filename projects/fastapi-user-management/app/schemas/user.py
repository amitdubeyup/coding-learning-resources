from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    is_active: bool = True


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)


class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=3, max_length=50)
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8, max_length=128)
    is_active: bool | None = None


class UserOut(UserBase):
    id: int
    created_at: datetime

    # Pydantic v2: replaces the deprecated `class Config: orm_mode = True`
    model_config = ConfigDict(from_attributes=True)


class UserInDB(UserOut):
    hashed_password: str
