"""a-step

Revision ID: 03d23a8e588b
Revises: 8064a150566c
Create Date: 2024-05-28 00:12:59.807503

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03d23a8e588b'
down_revision: Union[str, None] = '8064a150566c'
branch_labels: Union[str, Sequence[str], None] = 'step_a'
depends_on: Union[str, Sequence[str], None] = '8064a150566c'


def upgrade() -> None:
    op.add_column('users', sa.Column('bio', sa.String(), nullable=True))


def downgrade() -> None:
    pass