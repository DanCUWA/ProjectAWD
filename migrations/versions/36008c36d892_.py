"""empty message

Revision ID: 36008c36d892
Revises: 6f0a78a724c5
Create Date: 2023-05-12 13:30:35.055258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36008c36d892'
down_revision = '6f0a78a724c5'
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
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('roomID', sa.Integer(), nullable=False),
    sa.Column('roomName', sa.String(length=30), nullable=True),
    sa.Column('playerNumber', sa.Integer(), nullable=True),
    sa.Column('turnNumber', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('roomID'),
    sa.UniqueConstraint('roomID')
    )
    with op.batch_alter_table('game_room', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_game_room_username'), ['username'], unique=False)

    op.create_table('settings',
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('primaryColor', sa.String(length=7), nullable=True),
    sa.Column('secondaryColor', sa.String(length=7), nullable=True),
    sa.Column('textColour', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('stats',
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roomID', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('text', sa.String(length=500), nullable=True),
    sa.Column('time', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['roomID'], ['game_room.roomID'], ),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_message_roomID'), ['roomID'], unique=False)
        batch_op.create_index(batch_op.f('ix_message_username'), ['username'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_message_username'))
        batch_op.drop_index(batch_op.f('ix_message_roomID'))

    op.drop_table('message')
    op.drop_table('stats')
    op.drop_table('settings')
    with op.batch_alter_table('game_room', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_game_room_username'))

    op.drop_table('game_room')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))

    op.drop_table('user')
    # ### end Alembic commands ###