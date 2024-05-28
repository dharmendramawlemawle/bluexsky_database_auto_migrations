"""b-step

Revision ID: 3a86d67b0963
Revises: 03d23a8e588b
Create Date: 2024-05-28 00:33:08.709987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a86d67b0963'
down_revision: Union[str, None] = '03d23a8e588b'
branch_labels: Union[str, Sequence[str], None] = 'step_b'
depends_on: Union[str, Sequence[str], None] = '03d23a8e588b'


def upgrade() -> None:
    op.drop_column('users', 'bio')


def downgrade() -> None:
    pass
