import pytest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import create_app,db
from app.models import *
from app.main.main_controller import init_db,init_settings
@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    flask_app = create_app()
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()
    u1 = User(username="DCTEST")
    u1.set_password("abc")
    db.session.add(u1)
    init_settings(u1)

    u2 = User(username="GAMEMASTER")
    u2.set_password("no_login")
    db.session.add(u2)
    init_settings(u2)

    u3 = User(username="Test")
    u3.set_password("abc")
    db.session.add(u3)
    init_settings(u3)
    
    db.session.commit()
    yield  # this is where the testing happens!

    db.drop_all()
