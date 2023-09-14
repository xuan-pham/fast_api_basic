from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    fullname: str
    email: str
    password: str

