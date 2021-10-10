def test_settings(client):
    response = client.get("/settings")
    data = response.json()
    # overwritten in conftest.py
    assert data["app_name"] == "Test app name"
