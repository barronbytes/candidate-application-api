from datetime import datetime
from pydantic import BaseModel, EmailStr
from types import Optional


class Application(BaseModel):
    # Application Model
    id: int
    job_id: int
    candidate_name: str
    email: EmailStr
    resume_file_path: str
    cover_letter: Optional[str] = None
    submitted_date: datetime


    class Config:
        orm_mode = True
