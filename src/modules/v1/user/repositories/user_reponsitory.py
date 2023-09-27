from src.config.db.database import SessionLocal
from src.models import User
from src.schemas.sche_user import UserCreateRequest, UserUpdateRequest


class UserRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_list(self, skip: int, limit: int) -> list[User]:
        return self.db.query(User).offset(skip).limit(limit).all()

    def create(self, body: UserCreateRequest) -> User:
        db_user = User(**body.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user: User, body: UserUpdateRequest):
        for field, value in body.dict(exclude_unset=True).items():
            setattr(user, field, value)
        self.db.commit()
        self.db.refresh(user)

    def delete(self, user_id: int):
        db_user = self.db.query(User).get(user_id)
        self.db.delete(db_user)
        self.db.commit()
        self.db.refresh(db_user)
