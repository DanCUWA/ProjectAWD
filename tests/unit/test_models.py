from app.models import *
import pytest
def test_new_user(): 
    """
    GIVEN a new user model
    WHEN the user is created
    THEN validate its' fields
    """
    user = User(username="user1")
    user.set_password("abc") 
    assert user.username == "user1"
    assert user.password_hash != "abc"
    assert user.__repr__() == "<User user1, Room None>"
    assert user.is_authenticated

@pytest.fixture
def user():
    return User(username='testuser', roomID=1)


@pytest.fixture
def settings():
    return Settings(username='testuser', primaryColor='#ABCDEF')


@pytest.fixture
def game_room():
    return GameRoom(username='testuser', roomID=1, roomName='Test Room')


@pytest.fixture
def prompts():
    return Prompts(roomID=1, role='Test Role', content='Test Content')


@pytest.fixture
def message():
    return Message(roomID=1, username='testuser', text='Test Message')


def test_user_creation(user):
    assert user.username == 'testuser'
    assert user.roomID == 1


def test_settings_creation(settings):
    assert settings.username == 'testuser'
    assert settings.primaryColor == '#ABCDEF'


def test_game_room_creation(game_room):
    assert game_room.username == 'testuser'
    assert game_room.roomID == 1
    assert game_room.roomName == 'Test Room'


def test_prompts_creation(prompts):
    assert prompts.roomID == 1
    assert prompts.role == 'Test Role'
    assert prompts.content == 'Test Content'


def test_message_creation(message):
    assert message.roomID == 1
    assert message.username == 'testuser'
    assert message.text == 'Test Message'