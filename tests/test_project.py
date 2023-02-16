def test_response_with_valid_userid_get(client):
    response = client.get("/api/user/1")
    assert response.status_code == 200
    assert response.json["email"] == "john.doe@example.com"
    assert response.json["name"] == "John Doe"
    assert response.json["password"] == "Demo1"



def test_response_with_invalid_userid_get(client):
    response = client.get("/api/user/10")
    assert response.status_code == 404

def test_get_access_token(client):
    response = client.post("/login", json={"username": "John Doe", "password": "Demo1"})
    access_token = response.json["access_token"]


def test_response_with_valid_userid_post(client):
    response = client.post("/login", json={"username": "John Doe", "password": "Demo1"})
    access_token = response.json["access_token"]
    access_token_modified = "Bearer "+ access_token
    response = client.post("/api/user/10", headers={"Authorization": access_token_modified} ,json={"email": "test2.doe@example.com", "id": "10", "name": "ahuja", "password": "Demo1test"})
    assert response.status_code == 200