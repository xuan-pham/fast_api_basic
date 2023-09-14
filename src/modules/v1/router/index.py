from fastapi import APIRouter
from src.modules.v1.user.controllers import user_controller

router = APIRouter()

router.include_router(user_controller.router, tags=['user'], prefix='/user')
