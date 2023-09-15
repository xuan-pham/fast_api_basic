from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    fullname: str
    email: str


class UserCreateRequest(UserBase):
    email: str
    password: str


class UserUpdateRequest(UserBase):
    password: Optional[str] = None
