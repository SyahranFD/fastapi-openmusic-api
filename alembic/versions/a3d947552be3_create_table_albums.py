"""create table album

Revision ID: a3d947552be3
Revises: 
Create Date: 2024-09-15 18:28:18.664752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3d947552be3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'albums',
        sa.Column('id', sa.String(255), primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('albums')
