from fastapi import APIRouter, Depends
from . import users
from . import auth
from ..jwt import jwt_bearer

router = APIRouter()

router.include_router(users.router, tags=['user'], prefix='/user', dependencies=[Depends(jwt_bearer.JwtBearer())])
router.include_router(auth.router, tags=['auth'], prefix='/auth')
