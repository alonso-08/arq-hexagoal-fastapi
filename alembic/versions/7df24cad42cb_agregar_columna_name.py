"""Agregar columna name

Revision ID: 7df24cad42cb
Revises: ba1004442cab
Create Date: 2023-11-21 23:22:48.049043

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7df24cad42cb'
down_revision: Union[str, None] = 'ba1004442cab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('events', sa.Column('name', sa.String))


def downgrade() -> None:
    op.drop_column('events', 'name')
