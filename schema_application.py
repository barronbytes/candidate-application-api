from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict
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


    # Pydantic expect dictionary input by default
    # Setting from_attributes=True lets it accept ORM objects directly
    # This allows CustomClasses.model_validate(orm_instances) to work
    model_config = ConfigDict(from_attributes=True)
