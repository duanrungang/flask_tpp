"""empty message

Revision ID: 9901664c426a
Revises: dc3a1ad229c6
Create Date: 2019-12-18 14:42:31.584891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9901664c426a'
down_revision = 'dc3a1ad229c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('is_super', sa.Boolean(), nullable=True),
    sa.Column('permission', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_user')
    # ### end Alembic commands ###
