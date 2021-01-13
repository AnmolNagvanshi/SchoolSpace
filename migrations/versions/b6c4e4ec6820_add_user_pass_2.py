"""add user pass 2

Revision ID: b6c4e4ec6820
Revises: f94be9f9de02
Create Date: 2021-01-12 09:48:14.380070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6c4e4ec6820'
down_revision = 'f94be9f9de02'
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