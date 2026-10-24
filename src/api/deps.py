from src.db.session import SessionLocal
from typing import Generator
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from fastapi import Depends  , status , HTTPException
from src.models.user import User
from sqlalchemy.orm import Session
from jose import JWTError, jwt   #type:ignore
from src.core.config import settings


security = HTTPBearer()



def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
) -> User:
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload  = jwt.decode(token , settings.SECRET_KEY , algorithms=[settings.ALGORITHM])
        user_id : str = payload.get("sub")

        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user  =  db.query(User).filter(User.id == user_id)
    if user is None:
        raise credentials_exception

    return user