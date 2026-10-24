"""renombrar tabla user a users

Revision ID: 2c67a94721e4
Revises: 6dc6d9524a12
Create Date: 2026-10-24 14:31:22.620967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c67a94721e4'
down_revision: Union[str, Sequence[str], None] = '6dc6d9524a12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# OJO: esta migracion fue editada a mano.
# Alembic NO detecta renombres: el autogenerate proponia crear una tabla
# "users" vacia y BORRAR "user" con todos sus datos (create_table + drop_table).
# En su lugar renombramos la tabla, su indice y su llave primaria,
# asi los datos se conservan.


def upgrade() -> None:
    """Upgrade schema."""
    # 1. renombrar la tabla (los datos se quedan intactos)
    op.rename_table('user', 'users')
    # 2. renombrar el indice del email para que coincida con el modelo
    #    (si no, el proximo autogenerate querria borrarlo y crearlo de nuevo)
    op.execute('ALTER INDEX ix_user_email RENAME TO ix_users_email')
    # 3. renombrar la llave primaria para mantener los nombres consistentes
    op.execute('ALTER TABLE users RENAME CONSTRAINT user_pkey TO users_pkey')


def downgrade() -> None:
    """Downgrade schema."""
    # lo mismo pero al reves y en orden inverso
    op.execute('ALTER TABLE users RENAME CONSTRAINT users_pkey TO user_pkey')
    op.execute('ALTER INDEX ix_users_email RENAME TO ix_user_email')
    op.rename_table('users', 'user')
