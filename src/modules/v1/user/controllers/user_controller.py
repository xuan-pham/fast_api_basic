from fastapi import APIRouter
from ..services.user_service import UserService
from src.schemas.sche_user import UserCreateRequest

router = APIRouter()
user_service = UserService()


@router.get("")
async def get_list() -> dict:
    data = await user_service.get_list()
    return data


@router.post('create')
async def create_user(body: UserCreateRequest):
    data = await user_service.create(body)
    return data
