from sqlalchemy import Column , String , Text , DateTime , ForeignKey , func
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Post(Base):
    __tablename__ = "posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    # la fecha la pone postgres al insertar (server_default), con zona horaria
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # la llave foranea SIEMPRE vive en el lado "muchos" (posts)
    # SIN unique=True: un usuario puede tener muchos posts (esa es la diferencia con profile)
    # index=True: postgres NO crea indices automaticos en las llaves foraneas,
    # y vamos a buscar mucho "los posts de este usuario"
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # post.user -> devuelve el objeto User (el autor)
    user = relationship("User", back_populates="posts")
