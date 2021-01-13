"""add user pass

Revision ID: 4fb761978ed9
Revises: a634bdefdeb1
Create Date: 2021-01-12 09:44:50.089534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fb761978ed9'
down_revision = 'a634bdefdeb1'
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
