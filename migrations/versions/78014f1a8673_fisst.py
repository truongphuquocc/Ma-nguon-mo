"""fisst

Revision ID: 78014f1a8673
Revises: b9ee9d2ed8e8
Create Date: 2022-11-18 13:56:42.965114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78014f1a8673'
down_revision = 'b9ee9d2ed8e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###