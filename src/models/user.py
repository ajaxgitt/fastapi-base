from sqlalchemy import Column , String
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String)
    email = Column(String, unique=True, index=True)

    # user.profile -> devuelve UN objeto Profile (o None), no una lista
    # uselist=False es lo que le dice a SQLAlchemy que es uno a uno
    # cascade: si borras el usuario desde la sesion, tambien se borra su perfil
    profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )

    # user.posts -> devuelve una LISTA de Post (uno a muchos, sin uselist=False)
    posts = relationship(
        "Post",
        back_populates="user",
        cascade="all, delete-orphan",
    )