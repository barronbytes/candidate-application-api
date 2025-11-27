import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from typing import Generator


# SQLite database file (relative path)
DB_URL = "sqlite:///./model_app_jobs.db"

# Configure database connection
engine = sa.create_engine(DB_URL)

# Create database session for endpoint use
SessionLocal = sessionmaker(
    autocommit=False, # must use command session.commit() to save changes, can undeo changes with session.rollback()
    autoflush=False, # must use command session.flush() to query changes
    bind=engine
)


# Dependency function for FastAPI routes
def get_db() -> Generator[Session, None, None]:
    """
    Retrieves database session for FastAPI routes.
    Session closes once the API request ends.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Parent class for ORM models
class Base(DeclarativeBase):
    pass
