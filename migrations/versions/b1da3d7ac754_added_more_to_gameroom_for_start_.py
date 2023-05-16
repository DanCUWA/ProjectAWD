"""Added more to gameRoom for start scenario

Revision ID: b1da3d7ac754
Revises: 36008c36d892
Create Date: 2023-05-14 11:27:55.647101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1da3d7ac754'
down_revision = '36008c36d892'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game_room', schema=None) as batch_op:
        batch_op.add_column(sa.Column('scenario', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game_room', schema=None) as batch_op:
        batch_op.drop_column('scenario')

    # ### end Alembic commands ###
