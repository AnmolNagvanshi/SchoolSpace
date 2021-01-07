"""added bus & library

Revision ID: 290948282fa4
Revises: fce481b01066
Create Date: 2020-12-28 09:53:02.750461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290948282fa4'
down_revision = 'fce481b01066'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bus_route',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('bus_id', sa.Integer(), nullable=False),
    sa.Column('route', sa.String(length=128), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bus_route_bus_id'), 'bus_route', ['bus_id'], unique=False)
    op.create_table('library',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('book_name', sa.String(length=255), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('library')
    op.drop_index(op.f('ix_bus_route_bus_id'), table_name='bus_route')
    op.drop_table('bus_route')
    # ### end Alembic commands ###
