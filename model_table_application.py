import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship
from model_database import Base


class Application(Base):
    # Table for Application entity
    __tablename__ = "applications"

    # Primary key, auto-incrementing integer + Foreign key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)

    # Required fields
    candidate_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    resume_file_path = Column(String, nullable=False)
    submitted_date = Column(Date, default=datetime.date.today)

    # Optional fields
    cover_letter = Column(Text)

    # Relationship: one-job to many-applications
    job = relationship("Job", back_populates="applications")
