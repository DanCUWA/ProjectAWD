import pytest
from app.models import User
from flask import url_for
def test_home_page(test_client): 
    routes = ['/','/intro','/index','/signup','/login']
    for route in routes:
        response = test_client.get(route)
        assert response.status_code == 200

# def test_handleSignup(test_client, init_database):
#     response = test_client.post('/signup', data={
#         'username': 'new_user',
#         'password': 'password',
#         'password2': 'password',
#         'submit': 'Sign Up'
#     })
#     assert response.status_code == 302
#     assert response.headers['Location'] == url_for('login', _external=True)
#     # Add assertions for any expected behavior after successful form submission