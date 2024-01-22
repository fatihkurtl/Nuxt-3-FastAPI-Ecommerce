"""create order_cart table

Revision ID: 05ab4ff602ed
Revises: 0dd398c568c9
Create Date: 2024-01-16 10:15:52.737666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05ab4ff602ed'
down_revision: Union[str, None] = '0dd398c568c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'order_cart',
        sa.Column('order_id', sa.Integer, primary_key=True),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('products.id')),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('create_date', sa.DateTime)
    )
    pass


def downgrade() -> None:
    pass
