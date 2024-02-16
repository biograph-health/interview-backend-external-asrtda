from datetime import date

import freezegun
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app
from app.models import ReservationModel, TableModel

test_engine = create_engine(
    url="sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def get_test_db():
    """Returns a new database session."""
    db = TestingSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = get_test_db  # type: ignore[attr-defined]


@pytest.fixture
def client() -> TestClient:
    """A test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def db() -> TestingSession:
    """An initialized in-memory test database.

    This fixture drops and recreates the database tables between tests.
    """
    Base.metadata.create_all(bind=test_engine)
    yield from get_test_db()
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(autouse=True)
def setup_tables(db: TestingSession):
    """Adds 4 restaurant tables to the test database."""
    tables = (
        TableModel(seats=2),
        TableModel(seats=3),
        TableModel(seats=4),
        TableModel(seats=4),
    )
    db.add_all(tables)
    db.commit()


@pytest.fixture(autouse=True)
def setup_reservations(db: TestingSession):
    """Adds 4 reservations to the test database."""
    reservations = (
        ReservationModel(
            table_id=1,
            date=date(2024, 2, 16),
            time="17:30:00",
            name="jerry",
        ),
        ReservationModel(
            table_id=1,
            date=date(2024, 2, 16),
            time="19:00:00",
            name="elaine",
        ),
        ReservationModel(
            table_id=1,
            date=date(2024, 2, 16),
            time="20:30:00",
            name="george",
        ),
        ReservationModel(
            table_id=1,
            date=date(2024, 2, 23),
            time="20:30:00",
            name="kramer",
        ),
    )
    db.add_all(reservations)
    db.commit()


@pytest.fixture(autouse=True)
def freeze_system_time():
    """Set the current date to 2024-02-11."""
    freezegun.freeze_time("2024-02-11T12:00:00-05:00")
