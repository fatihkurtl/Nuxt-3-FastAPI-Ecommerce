"""create billing_details table

Revision ID: 86e3cc5fe0d6
Revises: 0b0830c03267
Create Date: 2024-01-19 15:00:24.099317

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86e3cc5fe0d6'
down_revision: Union[str, None] = '0b0830c03267'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'billing_details',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('firstname', sa.String),
        sa.Column('lastname', sa.String),
        sa.Column('country', sa.String),
        sa.Column('company_name', sa.String, nullable=True),
        sa.Column('street_address', sa.String),
        sa.Column('apartment_or_suite', sa.String, nullable=True),
        sa.Column('state_or_country', sa.String),
        sa.Column('posta_or_zip', sa.String),
        sa.Column('email', sa.String),
        sa.Column('phone', sa.String),
        sa.Column('order_notes', sa.String),
        sa.Column('order_id', sa.Integer, sa.ForeignKey('order_cart.order_id')),
        sa.Column('total_price', sa.Float),
        sa.Column('create_date', sa.DateTime),
    )
    pass


def downgrade() -> None:
    pass
