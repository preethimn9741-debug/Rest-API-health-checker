import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_home_page(client):
    res = client.get("/")
    assert res.status_code == 200

def test_get_items(client):
    res = client.get("/items")
    assert res.status_code == 200

def test_add_item_invalid(client):
    res = client.post("/items", json={})
    assert res.status_code == 400

def test_add_item_valid(client):
    res = client.post("/items", json={"name": "Test"})
    assert res.status_code == 201
