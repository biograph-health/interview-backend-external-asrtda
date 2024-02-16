import datetime

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ReservationModel
from app.schemas import ReservationRead, ReservationWrite

router = APIRouter()


@router.post(path="/reservations", response_model=ReservationRead)
def create_reservation(body: ReservationWrite, db: Session = Depends(get_db)):
    """Book a new reservation.

    If the reservation is already booked, return a 409 Conflict.
    """
    reservation = ReservationModel(**body.model_dump())

    try:
        db.add(reservation)
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Reservation already booked")

    db.refresh(reservation)
    return reservation


@router.get(path="/reservations", response_model=list[ReservationRead])
def list_reservations(date: datetime.date | None = None, db: Session = Depends(get_db)):
    """List all reservations.

    If a date is provided, only return reservations for that date.
    """
    query = db.query(ReservationModel)

    if date is not None:
        query = query.filter(ReservationModel.date == date)

    return query.all()


@router.get(path="/reservations/{reservation_id}", response_model=ReservationRead)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    """Get a specific reservation."""
    return db.get(ReservationModel, reservation_id)


@router.delete(path="/reservations/{reservation_id}", response_model=ReservationRead)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    """Delete a specific reservation."""
    reservation = db.get(ReservationModel, reservation_id)
    db.delete(reservation)
    db.commit()
    return reservation
