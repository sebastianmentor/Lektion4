"""Added Tidningar

Revision ID: 625642130946
Revises: ab1d27a6d6f1
Create Date: 2024-01-10 10:10:08.843656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '625642130946'
down_revision = 'ab1d27a6d6f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tidningar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titel', sa.String(length=80), nullable=False),
    sa.Column('forfattare', sa.String(length=50), nullable=False),
    sa.Column('pris', sa.Float(), nullable=False),
    sa.Column('lagerantal', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tidningar')
    # ### end Alembic commands ###
