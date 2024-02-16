from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models import TableModel


def test_create_table(client: TestClient, db: Session):
    response = client.post("/tables", json={"seats": 4})

    assert response.status_code == 200
    assert response.json() == {"id": 5, "seats": 4}
    assert db.query(TableModel).count() == 5


def test_list_tables(client: TestClient, db: Session):
    response = client.get("/tables")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "seats": 2},
        {"id": 2, "seats": 3},
        {"id": 3, "seats": 4},
        {"id": 4, "seats": 4},
    ]


def test_list_tables_by_seats(client: TestClient, db: Session):
    response = client.get("/tables?seats=4")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 3, "seats": 4},
        {"id": 4, "seats": 4},
    ]


def test_get_table(client: TestClient, db: Session):
    response = client.get("/tables/2")

    assert response.status_code == 200
    assert response.json() == {"id": 2, "seats": 3}


def test_delete_table(client: TestClient, db: Session):
    response = client.delete("/tables/2")

    assert response.status_code == 200
    assert response.json() == {"id": 2, "seats": 3}
    assert db.query(TableModel).count() == 3
