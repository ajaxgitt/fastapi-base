from sqlalchemy import Column , String
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Tag(Base):
    __tablename__ = "tags"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # no pueden existir dos etiquetas con el mismo nombre
    name = Column(String(50), unique=True, nullable=False)

    # tag.posts -> LISTA de Post que tienen esta etiqueta
    # secondary: la relacion pasa por la tabla intermedia post_tags
    posts = relationship("Post", secondary="post_tags", back_populates="tags")
