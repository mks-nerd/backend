from src.app import client

payload = {
    "name": "professional",
    "menu": [
        {"name": "Home", "endpoint": "/home"},
        {"name": "Task", "endpoint": "/task"},
    ],
}


def test_add_home():
    response = client.post(
        "/home/add_home",
        json=payload,
    )
    assert response.status_code == 200
    assert response.json() == payload

def test_get_home():
    response = client.get(
        "/home/get_home",
        params={"home_name":"professional"},
    )
    assert response.status_code == 200
    assert response.json() == [payload]

def test_delete_home():
    response = client.post(
        "/home/delete_home",
    )
    assert response.status_code == 200
    assert response.json() == "success"