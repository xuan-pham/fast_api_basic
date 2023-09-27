from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    fullname: str
    email: EmailStr


class UserCreateRequest(UserBase):
    password: str = Field(min_length=8)


class UserUpdateRequest(UserBase):
    pass
