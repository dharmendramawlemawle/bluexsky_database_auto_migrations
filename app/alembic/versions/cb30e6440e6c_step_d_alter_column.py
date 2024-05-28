"""step_d_alter_column

Revision ID: cb30e6440e6c
Revises: 82b5fa15a247
Create Date: 2024-05-28 00:58:45.374131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb30e6440e6c'
down_revision: Union[str, None] = '82b5fa15a247'
branch_labels: Union[str, Sequence[str], None] = 'step_d'
depends_on: Union[str, Sequence[str], None] = '82b5fa15a247'


def upgrade() -> None:
    op.add_column('posts', sa.Column('price', sa.Float(), nullable=True))
    with op.batch_alter_table('posts') as batch_op:
        batch_op.alter_column('price', type_=sa.TIMESTAMP, postgresql_using="price::timestamp")

def downgrade() -> None:
    
    with op.batch_alter_table('posts') as batch_op:
        batch_op.alter_column('price', type_=sa.Float, postgresql_using="price::float")