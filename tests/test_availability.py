from fastapi.testclient import TestClient


def test_list_available_dates(client: TestClient):
    response = client.get(
        "/availability/dates?start=2024-02-11&stop=2024-02-17&seats=2"
    )

    assert response.status_code == 200
    assert response.json() == [
        "2024-02-11",
        "2024-02-12",
        "2024-02-13",
        "2024-02-14",
        "2024-02-15",
        "2024-02-17",
    ]


def test_list_available_times(client: TestClient):
    response = client.get("/availability/times?date=2024-02-23&seats=2")

    assert response.status_code == 200
    assert response.json() == [
        {"table": {"id": 1, "seats": 2}, "time": "17:30:00"},
        {"table": {"id": 1, "seats": 2}, "time": "19:00:00"},
    ]
