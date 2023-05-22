import pytest
from flask import url_for
from app.models import User, Settings, Message, GameRoom

def test_user_anon(test_client):
    routes = ['/settings', '/profile', '/logout', '/get_username']
    for route in routes:
        response = test_client.get(route)
        assert response.status_code == 302

