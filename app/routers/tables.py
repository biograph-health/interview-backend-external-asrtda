from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import TableModel
from app.schemas import TableRead, TableWrite

router = APIRouter()


@router.post(path="/tables", response_model=TableRead)
def create_table(body: TableWrite, db: Session = Depends(get_db)):
    """Create a new table."""
    table = TableModel(**body.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table


@router.get(path="/tables", response_model=list[TableRead])
def list_tables(seats: int | None = None, db: Session = Depends(get_db)):
    """List all tables.

    If seats is provided, only return tables with that number of seats.
    """
    query = db.query(TableModel)

    if seats is not None:
        query = query.filter(TableModel.seats == seats)

    return query.all()


@router.get(path="/tables/{table_id}", response_model=TableRead)
def get_table(table_id: int, db: Session = Depends(get_db)):
    """Get a specific table."""
    return db.get(TableModel, table_id)


@router.delete(path="/tables/{table_id}", response_model=TableRead)
def delete_table(table_id: int, db: Session = Depends(get_db)):
    """Delete a specific table."""
    table = db.get(TableModel, table_id)
    db.delete(table)
    db.commit()
    return table
