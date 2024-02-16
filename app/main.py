from fastapi import FastAPI

from app.database import init_db
from app.routers import availability, reservations, tables

init_db()  # create the database tables

app = FastAPI()
app.include_router(availability.router)
app.include_router(reservations.router)
app.include_router(tables.router)
