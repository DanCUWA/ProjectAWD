import pytest
from flask import url_for
from app.models import User, Settings, Message, GameRoom

def test_user_anon(test_client):
    routes = ['/settings', '/profile', '/logout', '/get_username']
    for route in routes:
        response = test_client.get(route)
        assert response.status_code == 302

def test_register(test_client):
    assert test_client.get("/signup").status_code == 200

    data = {
        'username': 'test_user',
        'password': 'test_password',
    }
    response = test_client.post('/signup', data=data)
    assert response.status_code == 200

def test_login(test_client):
    assert test_client.get("/login").status_code == 200
    data = {
        'username': 'test_user',
        'password': 'test_password',
    }
    response = test_client.post('/login', data=data)
    assert response.status_code == 200

def test_setting_options(test_client):
    # Test case: Change username
    new_username = 'test_new_user'
    response = test_client.post('/settings', data={'username': new_username, 'username-submit': True})
    assert response.status_code == 302

    # Test case: Change password
    new_password = 'test_new_password'
    new_password2 = 'test_new_password2'
    response = test_client.post('/settings', data={'password1': new_password, 'password2': new_password2, 'password-submit': True})
    assert response.status_code == 302

    # Test case: Coloring
    primary_color = '#ffffff'
    secondary_color = '#ffffff'
    text_color = '#ffffff'
    response = test_client.post('/settings', data={'primColour': primary_color, 'secoColour': secondary_color, 'textColour': text_color, 'color-submit': True})
    assert response.status_code == 302
