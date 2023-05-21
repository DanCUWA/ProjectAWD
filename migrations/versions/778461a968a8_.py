"""empty message

Revision ID: 778461a968a8
Revises: 
Create Date: 2023-05-17 17:33:08.415209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '778461a968a8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_room',
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('roomID', sa.Integer(), nullable=False),
    sa.Column('roomName', sa.String(length=30), nullable=True),
    sa.Column('playerNumber', sa.Integer(), nullable=True),
    sa.Column('turnNumber', sa.Integer(), nullable=True),
    sa.Column('scenario', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('roomID'),
    sa.UniqueConstraint('roomID')
    )
    with op.batch_alter_table('game_room', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_game_room_username'), ['username'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('roomID', sa.Integer(), nullable=True),
    sa.Column('salt', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['roomID'], ['game_room.roomID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_roomID'), ['roomID'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roomID', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('text', sa.String(length=500), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['roomID'], ['game_room.roomID'], ),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_message_roomID'), ['roomID'], unique=False)
        batch_op.create_index(batch_op.f('ix_message_username'), ['username'], unique=False)

    op.create_table('prompts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roomID', sa.Integer(), nullable=True),
    sa.Column('role', sa.String(length=20), nullable=True),
    sa.Column('content', sa.String(length=400), nullable=True),
    sa.ForeignKeyConstraint(['roomID'], ['game_room.roomID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('prompts', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_prompts_roomID'), ['roomID'], unique=False)

    op.create_table('settings',
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('primaryColor', sa.String(length=7), nullable=True),
    sa.Column('secondaryColor', sa.String(length=7), nullable=True),
    sa.Column('textColor', sa.String(length=7), nullable=True),
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stats')
    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_settings_username'))

    op.drop_table('settings')
    with op.batch_alter_table('prompts', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_prompts_roomID'))

    op.drop_table('prompts')
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_message_username'))
        batch_op.drop_index(batch_op.f('ix_message_roomID'))

    op.drop_table('message')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_roomID'))

    op.drop_table('user')
    with op.batch_alter_table('game_room', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_game_room_username'))

    op.drop_table('game_room')
    # ### end Alembic commands ###
