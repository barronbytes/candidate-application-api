from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema_job import Job
from schema_application import Application, ApplicationCreate
from service_job import read_all_jobs
from service_application import create_application
from model_database import get_db


# Routes for users that are job applicants
router = APIRouter(prefix="/api", tags=["API"])


# Endpoint: GET /api/jobs
@router.get(path="/jobs", response_model=list[Job])
def read_all_jobs_route(db: Session = Depends(get_db)) -> list[Job]:
    """
    Handles HTTP GET requests at /api/jobs to return all active job posts from jobs table.

    Example usage:
        curl -X GET "http://127.0.0.1:8000/api/jobs" \
            -H "accept: application/json"
    """
    return read_all_jobs(db)


# Endpoint: POST api/applications
@router.post(path="/applications", response_model=Application)
def create_application_route(application: ApplicationCreate, db: Session = Depends(get_db)) -> Application:
    """
    Handles HTTP POST requests at /api/applications to save new job applications to applications table.

    Example Usage:
        curl -X POST "http://127.0.0.1:8000/api/applications" \
            -H "accept: application/json" \
            -H "Content-Type: application/json" \
            -d '{
                    "job_id": 1,
                    "candidate_name": "John Doe",
                    "email": "johndoe@candidate.com",
                    "resume_file_path": "/resumes/johndoe.pdf",
                    "cover_letter": "Dear...Sincerely, John."
                }'
    """
    return create_application(application, db)
