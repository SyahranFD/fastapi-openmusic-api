"""create table songs

Revision ID: 1a8c9e3d8d42
Revises: a3d947552be3
Create Date: 2024-09-15 18:37:10.442068

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a8c9e3d8d42'
down_revision: Union[str, None] = 'a3d947552be3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'songs',
        sa.Column('id', sa.String(255), primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.Column('performer', sa.String(255), nullable=False),
        sa.Column('genre', sa.String(255), nullable=False),
        sa.Column('duration', sa.Integer(), nullable=False),
        sa.Column('album_id', sa.String(255), sa.ForeignKey('albums.id', ondelete='CASCADE'), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('songs')
