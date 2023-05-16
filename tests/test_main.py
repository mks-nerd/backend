from src.main import client


def test_greet():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello"}
