from pydantic import BaseModel, EmailStr


class BaseAuth(BaseModel):
    email: EmailStr


class LoginRequest(BaseAuth):
    password: str


