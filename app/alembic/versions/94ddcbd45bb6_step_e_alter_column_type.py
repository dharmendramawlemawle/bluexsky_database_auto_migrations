"""step_e_alter_column_type

Revision ID: 94ddcbd45bb6
Revises: cb30e6440e6c
Create Date: 2024-05-28 01:33:46.817267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94ddcbd45bb6'
down_revision: Union[str, None] = 'cb30e6440e6c'
branch_labels: Union[str, Sequence[str], None] = 'step_e'
depends_on: Union[str, Sequence[str], None] = 'cb30e6440e6c'


def upgrade() -> None:
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('age', type_=sa.String, postgresql_using="age::text")


def downgrade() -> None:
     with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('age', type_=sa.Integer, postgresql_using="age::integer")
