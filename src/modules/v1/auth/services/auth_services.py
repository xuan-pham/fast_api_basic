from fastapi import HTTPException, status
from src.schemas import sche_auth
from src.modules.v1.user import UserRepository
from src.helpers import unit
from src.modules.v1.jwt import jwt_handler


class AuthService:

    def __init__(self):
        self.user_repo = UserRepository()

    def login(self, body: sche_auth.LoginRequest):
        user = self.user_repo.get_user_by_email(body.email)
        check_user = unit.authenticate_user(user, body)
        if not check_user:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = jwt_handler.create_access_token(user.id)
        return {"access_token": access_token, "token_type": "bearer"}
