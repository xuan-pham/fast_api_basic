from sqlalchemy import Boolean, Column, String
from .base import BareBaseModel


class User(BareBaseModel):
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
