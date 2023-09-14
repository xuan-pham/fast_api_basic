from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas import sche_user


class UserRepository:
    def __init__(self):
        self.db = Session()

    def create(self, body: sche_user.UserCreateRequest) -> sche_user.UserCreateRequest:
        db_user = User(**body.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return body
