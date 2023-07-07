from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from logger import Logger
from settings import settings
from fastapi.security.http import HTTPAuthorizationCredentials


def validate_request(token: HTTPAuthorizationCredentials = Depends(HTTPBearer())) -> bool:
    if token.credentials == settings.PASSWORD:
        return True
    Logger.error(f"validate_request - {token}")
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")
