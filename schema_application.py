from pydantic import BaseModel
from schema_job import Job


class Application(BaseModel):
    # Application Model
    job: Job
    candidate_name: str
    email: str
    resume_file_path: str
    cover_letter: str
    submitted_date: str
