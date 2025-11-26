from pydantic import BaseModel
from typing import Optional


class Job(BaseModel):
    # Job 
    id: int
    title: str
    department: str
    description: Optional[str] = None


    class Config:
        orm_mode = True
