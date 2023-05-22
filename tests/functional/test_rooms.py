def test_home_page(test_client): 
    routes = ['/rooms',"/rooms/deleteRoom",'/createRoom','/createRoom/created','/chat/<cur_room>']
    for route in routes:
        response = test_client.get(route)
        assert response.status_code == 302
    routes = ['/rooms/joinRoom']
    for route in routes:
        response = test_client.get(route)
        assert response.status_code == 405
