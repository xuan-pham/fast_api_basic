from passlib.context import CryptContext
from src.models import User
from ..schemas import sche_auth

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(user: User, data: sche_auth.LoginRequest) -> bool:
    if user.email == data.email and verify_password(plain_password=data.password, hashed_password=user.password):
        return True
    return False
