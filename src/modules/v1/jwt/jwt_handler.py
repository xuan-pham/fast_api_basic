import time
from fastapi import HTTPException, status
from jose import JWTError, jwt

from src.config.index import config


def token_response(token: str):
    return {
        'access_token': token
    }


def create_access_token(user_id: str):
    payload = {
        'userID': user_id,
        'expires': time.time()
    }
    token = jwt.encode(payload, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    return token


def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=config.JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else False
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
