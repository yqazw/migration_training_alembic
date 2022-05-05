"""Add a column

Revision ID: 233d4a5ec913
Revises: 3b971d475c7c
Create Date: 2022-05-04 09:44:05.452369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '233d4a5ec913'
down_revision = '3b971d475c7c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
