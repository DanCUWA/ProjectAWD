def test_home_page(test_client): 
    response = test_client.get('/')
    assert response.status_code == 200