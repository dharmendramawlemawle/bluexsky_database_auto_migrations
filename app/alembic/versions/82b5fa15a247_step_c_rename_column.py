"""seep_c_rename_column

Revision ID: 82b5fa15a247
Revises: 3a86d67b0963
Create Date: 2024-05-28 00:38:15.420247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82b5fa15a247'
down_revision: Union[str, None] = '3a86d67b0963'
branch_labels: Union[str, Sequence[str], None] = 'step_c'
depends_on: Union[str, Sequence[str], None] = '3a86d67b0963'


def upgrade() -> None:
    op.alter_column('users', 'username', new_column_name='user_name')


def downgrade() -> None:
    op.alter_column('users', 'user_name', new_column_name='username')
