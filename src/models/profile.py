from sqlalchemy import Column , String , Text , Date , ForeignKey
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bio = Column(Text)
    avatar_url = Column(String)
    birth_date = Column(Date)
    phone = Column(String(20))

    # la llave foranea vive en profiles y apunta a users.id
    # unique=True es lo que hace la relacion UNO a UNO: un usuario no puede tener 2 perfiles
    # ondelete="CASCADE": si se borra el usuario, postgres borra su perfil
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    # profile.user -> devuelve el objeto User
    user = relationship("User", back_populates="profile")
