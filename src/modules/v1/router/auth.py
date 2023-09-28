from fastapi import APIRouter
from src.schemas import sche_auth
from ..auth import AuthService

router = APIRouter()
auth_service = AuthService()


@router.post('/login')
def login(body: sche_auth.LoginRequest):
    return auth_service.login(body)
