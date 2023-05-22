import pytest
from app.models import User

def test_home_page(test_client): 
    routes = ['/','/intro','/index','/signup','/login']
    for route in routes:
        response = test_client.get(route)
        assert response.status_code == 200

