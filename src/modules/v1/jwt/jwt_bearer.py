from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from . import jwt_handler


class JwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JwtBearer, self).__call__(request)
        if not credentials.scheme == 'Bearer' and self.verify_jwt(credentials.credentials):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid or Expired Token2')
        return credentials.credentials

    def verify_jwt(self, jwt_token: str):
        is_token_valid: bool = False
        payload = jwt_handler.decode_jwt(jwt_token)
        if payload:
            is_token_valid = True
        return is_token_valid
