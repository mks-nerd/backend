from src.main import client


payload = {
    "first_name": "Mohan",
    "last_name": "Sahu",
    "age": 28,
    "likes": ["Programming", "Sudoku", "Cooking"],
}


def test_greet():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello"}


def test_add_user():
    response = client.post(
        "/add_user",
        json=payload,
    )
    assert response.status_code == 200
    assert response.json() == payload


def test_remove_user():
    response = client.post(
        "/remove_user",
        json=payload,
    )
    assert response.status_code == 200
    assert response.json() == payload
