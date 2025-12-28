import pytest
from app import app, add_numbers, subtract_numbers


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
    assert b"4 + 6 = 10" in response.data

def test_subtraction_flow(client):
    response = client.post("/", data={"num1": "14", "num2": "6"})
    assert b"14 - 6 = 8" in response.data

def test_subtract_numbers():
    assert subtract_numbers(8, 3) == 5
    assert subtract_numbers(-1, 1) == -2

