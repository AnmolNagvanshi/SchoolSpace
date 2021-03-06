"""email teacher unique

Revision ID: 92225e67047b
Revises: 17dfa0252c2d
Create Date: 2021-01-12 09:10:22.054389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92225e67047b'
down_revision = '17dfa0252c2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teacher', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.create_index(op.f('ix_teacher_email'), 'teacher', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_teacher_email'), table_name='teacher')
    op.alter_column('teacher', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###
