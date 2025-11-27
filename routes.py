from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema_job import Job
from service_job import read_all_jobs
from model_database import get_db


# Routes for users that are job applicants
router = APIRouter(prefix="/api", tags=["API"])


# Endpoint: GET /api/jobs
@router.get(path="/jobs", response_model=list[Job])
def read_all_jobs_route(db: Session = Depends(get_db)) -> list[Job]:
    """
    Handles HTTP GET requests at /api/jobs to return all active job posts.

    Example usage:
        curl -X GET "http://127.0.0.1:8000/api/jobs" \
          -H "accept: application/json"
    """
    return read_all_jobs(db)