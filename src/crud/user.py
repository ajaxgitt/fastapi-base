from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserCreate

def get_users (db:Session):
    db_users = db.query(User).all()
    return db_users

def created_user( data:UserCreate , db:Session):
    db_user = User(
        username = data.username,
        email = data.email,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user) 
    return db_user