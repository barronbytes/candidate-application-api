from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from model_database import Base


class Job(Base):
    # Table for Job entity
    __tablename__ = "jobs"

    # Primary key, auto-incrementing integer
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Required fields
    title = Column(String, nullable=False)
    department = Column(String, nullable=False)

    # Optional fields
    description = Column(Text)

    # Relationship: one-job to many-applications
    applications = relationship("Application", back_populates="job")
