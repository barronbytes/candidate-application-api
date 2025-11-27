from pydantic import BaseModel, ConfigDict
from typing import Optional


class Job(BaseModel):
    # Job 
    id: int
    title: str
    department: str
    description: Optional[str] = None


    # Pydantic expect dictionary input by default
    # Setting from_attributes=True lets it accept ORM objects directly
    # This allows CustomClasses.model_validate(orm_instances) to work
    model_config = ConfigDict(from_attributes=True)
