import pytest
from flask import url_for
from app.models import User, Settings, Message, GameRoom

def test_user_anon(test_client):
    routes = ['/settings', '/profile', '/logout', '/get_username']
    for route in routes:
        response = test_client.get(route)
        assert response.status_code == 302

# def test_user_on(test_client, init_database): 
#     user = User.query.all()[0]
#     assert user is not None
#     response = test_client.post('/login')
