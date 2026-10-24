from sqlalchemy import Column , DateTime , ForeignKey , UniqueConstraint , func
from src.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


# TABLA INTERMEDIA del muchos a muchos entre posts y tags
# ni posts ni tags pueden guardar una lista de llaves foraneas,
# por eso cada fila de esta tabla representa UN vinculo post <-> tag
class PostTag(Base):
    __tablename__ = "post_tags"

    # como esta tabla tiene su propio id (igual que el resto del proyecto),
    # el id NO evita duplicados: sin esta regla se podria poner
    # la misma etiqueta dos veces al mismo post
    __table_args__ = (
        UniqueConstraint("post_id", "tag_id", name="uq_post_tag"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # ondelete="CASCADE": si se borra el post o la etiqueta, se borra el vinculo
    # (la etiqueta NO se borra al borrar un post, solo el vinculo)
    post_id = Column(
        UUID(as_uuid=True),
        ForeignKey("posts.id", ondelete="CASCADE"),
        nullable=False,
    )
    # index=True: el UniqueConstraint ya crea un indice que empieza por post_id,
    # pero para buscar "los posts de una etiqueta" necesitamos uno por tag_id
    tag_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tags.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # columna extra: la ventaja de tener un modelo y no una tabla simple
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
