from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models import ReservationModel


def test_create_reservation(client: TestClient, db: Session):
    response = client.post(
        url="/reservations",
        json={
            "table_id": 4,
            "date": "2024-02-23",
            "time": "19:00:00",
            "name": "newman",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 5,
        "date": "2024-02-23",
        "time": "19:00:00",
        "table": {"id": 4, "seats": 4},
        "name": "newman",
    }
    assert db.query(ReservationModel).count() == 5


def test_create_duplicate_reservation(client: TestClient):
    response = client.post(
        url="/reservations",
        json={
            "table_id": 1,
            "date": "2024-02-23",
            "time": "20:30:00",
            "name": "newman",
        },
    )

    assert response.status_code == 409
    assert response.json() == {"detail": "Reservation already booked"}


def test_list_reservations(client: TestClient):
    response = client.get("/reservations")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "date": "2024-02-16",
            "time": "17:30:00",
            "name": "jerry",
            "table": {"id": 1, "seats": 2},
        },
        {
            "id": 2,
            "date": "2024-02-16",
            "time": "19:00:00",
            "name": "elaine",
            "table": {"id": 1, "seats": 2},
        },
        {
            "id": 3,
            "date": "2024-02-16",
            "time": "20:30:00",
            "name": "george",
            "table": {"id": 1, "seats": 2},
        },
        {
            "id": 4,
            "date": "2024-02-23",
            "time": "20:30:00",
            "name": "kramer",
            "table": {"id": 1, "seats": 2},
        },
    ]


def test_list_reservations_by_date(client: TestClient):
    response = client.get("/reservations?date=2024-02-16")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "date": "2024-02-16",
            "time": "17:30:00",
            "name": "jerry",
            "table": {"id": 1, "seats": 2},
        },
        {
            "id": 2,
            "date": "2024-02-16",
            "time": "19:00:00",
            "name": "elaine",
            "table": {"id": 1, "seats": 2},
        },
        {
            "id": 3,
            "date": "2024-02-16",
            "time": "20:30:00",
            "name": "george",
            "table": {"id": 1, "seats": 2},
        },
    ]


def test_get_reservation(client: TestClient, db: Session):
    response = client.get("/reservations/2")

    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "date": "2024-02-16",
        "time": "19:00:00",
        "name": "elaine",
        "table": {"id": 1, "seats": 2},
    }


def test_delete_reservation(client: TestClient, db: Session):
    response = client.delete("/reservations/2")

    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "date": "2024-02-16",
        "time": "19:00:00",
        "name": "elaine",
        "table": {"id": 1, "seats": 2},
    }
    assert db.query(ReservationModel).count() == 3
