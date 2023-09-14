from fastapi import APIRouter
from ..services.user_service import UserService
from src.schemas.sche_user import UserCreateRequest

router = APIRouter()
user_service = UserService()


@router.get('/{user_id}')
def index(user_id: int):
    data = user_service.get_id(user_id)
    return data


@router.get('')
def show(skip: int = 0, limit: int = 100):
    data = user_service.get_list(skip, limit)
    return data


@router.post('/create')
def create(body: UserCreateRequest):
    data = user_service.create(body)
    return data


@router.put('/update/{user_id}')
def update(body):
    data = user_service.update(body)
    return data


@router.delete('/delete/{user_id}')
def destroy(user_id: int):
    data = user_service.remove(user_id)
    return data
