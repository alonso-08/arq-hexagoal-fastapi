"""Crear la primera tabla

Revision ID: ba1004442cab
Revises: 
Create Date: 2023-11-21 23:20:28.807108

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba1004442cab'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'events',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('start_date', sa.String),
        sa.Column('end_date', sa.String),
        sa.Column('cancelled', sa.Boolean, default=False)
    )


def downgrade() -> None:
    op.drop_table('events')
