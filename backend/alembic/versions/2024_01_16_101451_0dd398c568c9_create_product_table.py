"""create product table

Revision ID: 0dd398c568c9
Revises: 
Create Date: 2024-01-16 10:14:51.670550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0dd398c568c9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('price', sa.Float(200)),
        sa.Column('image_url', sa.String(200)),
        sa.Column('create_date', sa.DateTime)
    )
    pass


def downgrade() -> None:
    pass
