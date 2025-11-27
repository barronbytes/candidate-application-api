import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, sessionmaker


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

# Parent class for ORM models
class Base(DeclarativeBase):
    pass
