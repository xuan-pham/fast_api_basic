from fastapi import HTTPException, status
from src.schemas import sche_user
from ..repositories.user_reponsitory import UserRepository
from src.helpers.unit import hash_pass


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    async def get_list(self):
        return {'data': 'get list'}

    async def create(self, body: sche_user.UserCreateRequest):
        try:
            new_pass = hash_pass(body.password)
            body.password = new_pass
            result = await self.user_repo.create(body=body)

            # if result:
            #     raise HTTPException(status_code=400, detail="Email already registered")

            return result
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
