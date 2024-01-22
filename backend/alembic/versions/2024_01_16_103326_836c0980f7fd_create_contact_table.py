"""create contact table

Revision ID: 836c0980f7fd
Revises: 05ab4ff602ed
Create Date: 2024-01-16 10:33:26.410279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '836c0980f7fd'
down_revision: Union[str, None] = '05ab4ff602ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'contact',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('firstname', sa.String, nullable=False),
        sa.Column('lastname', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('message', sa.String, nullable=False),
        sa.Column('send_date', sa.DateTime)
    )
    pass


def downgrade() -> None:
    pass
