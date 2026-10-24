from fastapi import APIRouter, Response , Depends , HTTPException
from src.schemas.auth import DataLogin ,LoginResponse
from sqlalchemy.orm import Session
from src.api.deps import get_db
from src.services.auth import authenticate_user , create_access_token
from src.models.user import User
from datetime import timedelta
from src.core.config import settings

router= APIRouter()


#TODO aumentar el password al modelo user para que esto funcione

@router.post('/login' , response_model=LoginResponse)
def login_for_access_token (data:DataLogin, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.username).first()
    if user_db is None:
        raise HTTPException(status_code=400, detail=[
            {"field": "identifier", "message": "Credenciales inválidas"}
        ])

    user = authenticate_user(
        username=user_db.username,
        password=data.password,
        db=db
    )
    if user is None:
        raise HTTPException(status_code=400, detail=[
                {"field": "password",
                    "message": f"Credenciales inválidas."}
            ]) 
    else:
        access_token_expires = timedelta(
                    minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        access_token = create_access_token(
                    data={"sub": str(user.id)}, expires_delta=access_token_expires
                )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }
