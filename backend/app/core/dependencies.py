from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from jose import jwt
from fastapi import HTTPException
from fastapi import Depends
from jose import JWTError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.JWT_Secret, algorithms=[settings.JWT_Algorithm])
        return  payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")