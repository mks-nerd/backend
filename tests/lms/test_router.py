from datetime import date

from tests import client


def test_apply():
    payload = {
        "applicant_id": "1",
        "start_date": date(2023, 6, 14).isoformat(),
        "end_date": date(2023, 6, 14).isoformat(),
        "reason": "test",
    }
    response = client.post(
        "/lms/apply",
        json=payload,
    )
    assert response.status_code == 200
    assert response.json() == payload


def test_add_holiday():
    payload = {
        "holiday_name": "test",
        "holiday_date": date(2023, 6, 14).isoformat(),
    }
    response = client.post(
        "/lms/add_holiday",
        json=payload,
    )
    assert response.status_code == 200
    assert response.json() == payload


def test_get_holidays():
    payload = {
        "holiday_name": "test",
        "holiday_date": date(2023, 6, 14).isoformat(),
    }
    response = client.get(
        "/lms/get_holidays",
    )
    assert response.status_code == 200
    assert response.json() == [payload]


def test_add_weekend():
    payload = {"weekends": ["saturday"]}
    response = client.post(
        "/lms/add_weekend",
        json=payload,
    )
    assert response.status_code == 200
    assert response.json() == payload


def test_get_weekends():
    payload = {"weekends": ["saturday"]}
    response = client.get(
        "/lms/get_weekends",
    )
    assert response.status_code == 200
    assert response.json() == [payload]
