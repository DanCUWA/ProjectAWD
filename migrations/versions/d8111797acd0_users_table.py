"""users table

Revision ID: d8111797acd0
Revises: 
Create Date: 2023-04-30 13:42:27.094679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8111797acd0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('salt', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('game_room',
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('roomID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('username')
    )
    with op.batch_alter_table('game_room', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_game_room_roomID'), ['roomID'], unique=True)
        batch_op.create_index(batch_op.f('ix_game_room_username'), ['username'], unique=False)

    op.create_table('settings',
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('primaryColor', sa.String(length=7), nullable=True),
    sa.Column('secondaryColor', sa.String(length=7), nullable=True),
    sa.Column('textColour', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('username')
    )
    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_settings_username'), ['username'], unique=False)

    op.create_table('stats',
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('username')
    )
    with op.batch_alter_table('stats', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_stats_username'), ['username'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stats', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_stats_username'))

    op.drop_table('stats')
    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_settings_username'))

    op.drop_table('settings')
    with op.batch_alter_table('game_room', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_game_room_username'))
        batch_op.drop_index(batch_op.f('ix_game_room_roomID'))

    op.drop_table('game_room')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))

    op.drop_table('user')
    # ### end Alembic commands ###
