"""add user pass 3

Revision ID: 3cd1dbc6c4ba
Revises: ba86a8c89f5f
Create Date: 2021-01-12 09:50:55.972158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cd1dbc6c4ba'
down_revision = 'ba86a8c89f5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('password', sa.String(length=512), nullable=False))
    op.add_column('teacher', sa.Column('username', sa.String(length=512), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teacher', 'username')
    op.drop_column('teacher', 'password')
    # ### end Alembic commands ###