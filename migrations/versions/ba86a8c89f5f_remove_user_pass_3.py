"""remove user pass 3

Revision ID: ba86a8c89f5f
Revises: b6c4e4ec6820
Create Date: 2021-01-12 09:50:05.159386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba86a8c89f5f'
down_revision = 'b6c4e4ec6820'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teacher', 'username')
    op.drop_column('teacher', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('password', sa.VARCHAR(length=512), autoincrement=False, nullable=False))
    op.add_column('teacher', sa.Column('username', sa.VARCHAR(length=512), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
