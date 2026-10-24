from sqlalchemy.orm import Session 
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext  #type:ignore
from fastapi import HTTPException, status
from src.models.user import User
from datetime import datetime , timedelta , timezone
from src.core.config import settings
from jose import JWTError, jwt  #type:ignore



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=15) #<-- expira cada 15 minutos
    )
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)



def authenticate_user(username: str, password: str, db: Session):
    try:
        user = (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

        if user is None:
            return False

        if not pwd_context.verify(password, user.password):
            return False

        return user

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during authentication"
        )

