"""empty message

Revision ID: f6687e98954e
Revises: b3ddd68598d8
Create Date: 2019-12-19 15:53:17.169146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6687e98954e'
down_revision = 'b3ddd68598d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('o_user_id', sa.Integer(), nullable=True),
    sa.Column('o_hall_movie_id', sa.Integer(), nullable=True),
    sa.Column('o_time', sa.DateTime(), nullable=True),
    sa.Column('o_status', sa.Integer(), nullable=True),
    sa.Column('o_seats', sa.String(length=128), nullable=True),
    sa.Column('o_price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['o_hall_movie_id'], ['hall_movie.id'], ),
    sa.ForeignKeyConstraint(['o_user_id'], ['movie_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('h_num', table_name='hall')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('h_num', 'hall', ['h_num'], unique=True)
    op.drop_table('movie_order')
    # ### end Alembic commands ###