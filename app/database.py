from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

engine = create_engine(
    url="sqlite:////tmp/app.db", connect_args={"check_same_thread": False}
)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db() -> None:
    """Creates the database tables.

    We're not running database migrations as we would do in a real project. Instead,
    we'll set up the database tables when we start the app.
    """
    Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    """A dependency that returns a new database session."""
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
