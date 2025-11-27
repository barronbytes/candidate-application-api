import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# SQLite database file (relative path)
DB_URL = "sqlite:///./model_app_jobs.db"

# Configure database connection
engine = sa.create_engine(
    DB_URL,
    connect_args={"check_same_thread": False}
)

# Create database session for endpoint use
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Parent class for ORM models
class Base(DeclarativeBase):
    pass
