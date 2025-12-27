import pytest
from app import app, add_numbers


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_addition_flow(client):
    response = client.post("/", data={"num1": "4", "num2": "6"})
    assert b"10" in response.data
