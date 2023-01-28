def test_request_example(client):
    response = client.get("/api/user/1")
    assert response.status_code == 200
    assert response.json["email"] == "john.doe@example.com"
