from passlib.context import CryptContext
from jose import jwt
from app.core.config import settings
from datetime import datetime, timedelta

pwd_context = CryptContext(
    schemes=["bcrypt"],           # Use bcrypt hashing
    deprecated="auto",            # Automatically mark old schemes as deprecated
    bcrypt__rounds=12             # Cost factor (higher = slower but more secure)
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(Plained_password: str, hashed_password: str ) -> bool:
      return pwd_context.verify(Plained_password,hashed_password)

def create_access_token(email: str, role: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {"email": email, "role": role, "exp": expire}
    return jwt.encode(data, settings.JWT_Secret, algorithm=settings.JWT_Algorithm)