"""empty message

Revision ID: a4d57df40334
Revises: 31cec7c2e568
Create Date: 2019-12-18 20:34:47.712935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4d57df40334'
down_revision = '31cec7c2e568'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinema_address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_user', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=16), nullable=True),
    sa.Column('district', sa.String(length=16), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('hallnum', sa.Integer(), nullable=True),
    sa.Column('servicecharge', sa.Float(), nullable=True),
    sa.Column('astrict', sa.Float(), nullable=True),
    sa.Column('flag', sa.Boolean(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['c_user'], ['cinema_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinema_address')
    # ### end Alembic commands ###
