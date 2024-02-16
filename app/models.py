from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import Date, Integer, String

from app.database import Base


class TableModel(Base):
    """A restaurant table.

    Each table has a specific number of seats. This determines which parties can be
    seated there.
    """

    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    seats = Column(Integer)

    reservations = relationship("ReservationModel", back_populates="table")


class ReservationModel(Base):
    """A reservation for a specific table at a specific date and time.

    Each reservation is made under someone's name. It is associated with a specific
    table, date and time. No two reservations can be made for the same table at the
    same date and time.
    """

    __tablename__ = "reservations"
    __table_args__ = (UniqueConstraint("table_id", "date", "time"),)

    id = Column(Integer, primary_key=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    date = Column(Date)
    time = Column(String)
    name = Column(String)

    table = relationship("TableModel", back_populates="reservations", lazy="joined")
