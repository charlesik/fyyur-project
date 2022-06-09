"""empty message

Revision ID: eaab8677356d
Revises: cc549e5d5589
Create Date: 2022-06-06 18:20:32.397434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaab8677356d'
down_revision = 'cc549e5d5589'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('Venue', sa.Column('created_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'created_at')
    op.drop_column('Artist', 'created_at')
    # ### end Alembic commands ###