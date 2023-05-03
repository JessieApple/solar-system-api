import pytest

def test_get_all_planets_with_no_records(client):
    response = client.get('/planets')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == []
    
def test_get_all_planets_with_records(client,two_planets):
    response = client.get('/planets')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == [{
        'id':1,
        'name':"Earth", 
        'description':"Kinda cool", 
        'has_humans':True
        },
        {
        'id':2,
        'name':"Pluto", 
        'description':"It's a planet", 
        'has_humans':False 
        }]
    
def test_get_one_planet(client,two_planets):
    response = client.get('/planets/1')
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {
        'id':1,
        'name':"Earth", 
        'description':"Kinda cool", 
        'has_humans':True
        }
    
def test_get_planet_not_exist(client):
    response = client.get('/planets/1')
    
    assert response.status_code == 404
    assert "Not Found" in response 