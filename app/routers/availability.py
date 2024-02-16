import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import AvailabilityRead

router = APIRouter()


@router.get(path="/availability/dates", response_model=list[datetime.date])
def list_available_dates(
    start: datetime.date, stop: datetime.date, seats: int, db: Session = Depends(get_db)
):
    """Lists ISO-formatted dates with available reservations.

    Expects three query parameters:
      - start: the first date (inclusive) in the date range
      - stop: the last date (inclusive) in the date range
      - seats: the number of seats to return availability for

    Example:
        [
            "2022-01-01",
            "2022-01-02",
            "2022-01-04"
        ]
    """
    raise NotImplementedError


@router.get(path="/availability/times", response_model=list[AvailabilityRead])
def list_available_times(
    date: datetime.date, seats: int, db: Session = Depends(get_db)
):
    """Lists the available tables and times for a given date.

    Expects two query parameters:
      - date: the date to return availability for
      - seats: the number of seats to return availability for

    Example:
        [
               {
                    "table": { "id": 1, "seats": 4 },
                    "time": "17:00:00"
                },
                {
                    "table": { "id": 2, "seats": 4 },
                    "time": "17:00:00"
                },
                {
                    "table": { "id": 2, "seats": 4 },
                    "time": "18:30:00"
                }
        ]
    """
    raise NotImplementedError
