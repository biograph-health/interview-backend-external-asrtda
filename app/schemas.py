from datetime import date
from enum import Enum

from pydantic import BaseModel


class TimeSlot(str, Enum):
    """A set of possible reservation times.

    For simplicity, these are the only times available for reservations.
    Note that this enum is iterable, so you can do things like:

        for time in TimeSlot:
           ...
    """

    A = "17:30:00"
    B = "19:00:00"
    C = "20:30:00"


class TableRead(BaseModel):
    """The table schema returned in responses.

    Example:
        {
            "id": 1,
            "seats": 4
        }
    """

    id: int
    seats: int


class TableWrite(BaseModel):
    """The table schema expected in request bodies.

    Example:
        {
            "seats": 4
        }
    """

    seats: int


class ReservationRead(BaseModel):
    """The reservation schema returned in responses.

    Example:
        {
            "id": 1,
            "table": {
                "id": 1,
                "seats": 4
            },
            "date": "2024-02-16",
            "time": "17:30:00",
            "name": "jerry"
        }
    """

    id: int
    table: TableRead
    date: date
    time: TimeSlot
    name: str


class ReservationWrite(BaseModel):
    """The reservation schema expected in request bodies.

    Example:
        {
            "table_id": 1,
            "date": "2024-02-16",
            "time": "17:30:00",
            "name": "jerry"
        }
    """

    table_id: int
    date: date
    time: TimeSlot
    name: str


class AvailabilityRead(BaseModel):
    """The availability schema returned in responses.

    Example:
        {
            "table": {
                "id": 1,
                "seats": 4
            },
            "time": "17:30:00"
        }
    """

    table: TableRead
    time: TimeSlot
