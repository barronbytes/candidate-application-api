from pydantic import BaseModel


class Job(BaseModel):
    # Job Model
    title: str
    department: str
    description: str
