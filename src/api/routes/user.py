from fastapi import APIRouter , Depends
from src.api.deps import get_db , get_current_user
from sqlalchemy.orm import Session
from src.schemas.user import UserResponse , UserCreate
from typing import List
from src.models.user import User
from src.crud import user as user_crud


router = APIRouter()


@router.get("", response_model=List[UserResponse])
def get_users(db:Session=Depends(get_db) , current_user:User = Depends(get_current_user)):
    return user_crud.get_users(db)


@router.post("", response_model=UserResponse)
def created_user( data :UserCreate ,  db:Session = Depends(get_db)):
    return user_crud.created_user(data=data , db=db)