"""remove joining

Revision ID: 27dd7f7878d1
Revises: 92225e67047b
Create Date: 2021-01-12 09:38:37.806180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27dd7f7878d1'
down_revision = '92225e67047b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teacher', 'joining_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('joining_date', sa.DATE(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###