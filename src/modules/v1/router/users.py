from fastapi import APIRouter, Query, Path, Depends
from typing import Annotated
from src.schemas.sche_user import UserCreateRequest, UserUpdateRequest, UserBase
from ..user import UserService

router = APIRouter()
user_service = UserService()


@router.get('')
def show(skip: Annotated[int, Query()] = 0, limit: Annotated[int, Query()] = 100):
    data = user_service.get_list(skip, limit)
    return data


@router.get('/{user_id}')
def index(user_id: Annotated[int, Path(ge=1)]):
    data = user_service.get_id(user_id)
    return data


@router.post('/create')
def create(body: UserCreateRequest) -> UserBase:
    data = user_service.create(body)
    return data


@router.put('/update/{user_id}')
def update(user_id: int, body: UserUpdateRequest):
    data = user_service.update(user_id, body)
    return data


@router.delete('/delete/{user_id}')
def destroy(user_id: int):
    data = user_service.remove(user_id)
    return data
