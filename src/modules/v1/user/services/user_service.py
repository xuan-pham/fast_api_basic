from fastapi import HTTPException, status
from src.schemas import sche_user
from ..repositories.user_reponsitory import UserRepository
from src.helpers.unit import hash_pass


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def get_id(self, user_id: int):
        try:
            data = self.user_repo.get_user_by_id(user_id)
            return data
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err)
            )

    def get_list(self, skip: int, limit: int):
        try:
            data = self.user_repo.get_list(skip, limit)
            return data
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err)
            )

    def create(self, body: sche_user.UserCreateRequest):
        try:
            new_pass = hash_pass(body.password)
            body.password = new_pass

            check_user = self.user_repo.get_user_by_email(body.email)
            if check_user:
                return HTTPException(status_code=400, detail="Email already registered")

            result = self.user_repo.create(body=body)
            return result
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err)
            )

    def update(self, body):
        try:
            data = self.user_repo.update(body)
            return data
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err)
            )

    def remove(self, user_id: int):
        try:
            check_user = self.user_repo.get_user_by_id(user_id)
            if not check_user:
                return HTTPException(status_code=404, detail="User not found")

            self.user_repo.delete(user_id)
            return HTTPException(
                status_code=status.HTTP_200_OK,
                detail='Delete user successfully'
            )
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(err)
            )
