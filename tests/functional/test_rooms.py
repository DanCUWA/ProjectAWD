import pytest
from app.models import User
from flask import url_for

def test_room_page(test_client):
        route = test_client.get('/rooms')
        assert route.status_code == 302

# def test_room_text(test_client):
#         route = test_client.get('/rooms')
#         assert b"""<h1 style="color:white">GameRooms</h1>""" in route.data
#         assert b"@2023 Copyright" in route.data
#         assert b"Settings" in route.data
