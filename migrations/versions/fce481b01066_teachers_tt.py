"""teachers tt

Revision ID: fce481b01066
Revises: b2ea58513db1
Create Date: 2020-12-27 19:52:39.930774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fce481b01066'
down_revision = 'b2ea58513db1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers_time_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('class_1', sa.String(length=64), nullable=True),
    sa.Column('class_2', sa.String(length=64), nullable=True),
    sa.Column('class_3', sa.String(length=64), nullable=True),
    sa.Column('class_4', sa.String(length=64), nullable=True),
    sa.Column('remaining_slots', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teachers_time_table_teacher_id'), 'teachers_time_table', ['teacher_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_teachers_time_table_teacher_id'), table_name='teachers_time_table')
    op.drop_table('teachers_time_table')
    # ### end Alembic commands ###