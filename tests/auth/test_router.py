from main import client

payload = {
    "first_name": "Mohan",
    "last_name": "Sahu",
    "age": 28,
    "likes": ["Programming", "Sudoku", "Cooking"],
}


def test_add_user():
    response = client.post(
        "/auth/add_user",
        json=payload,
    )
    assert response.status_code == 200
    assert response.json() == payload


def test_remove_user():
    response = client.post(
        "/auth/remove_user",
        json=payload,
    )
    assert response.status_code == 200
    assert response.json() == payload
