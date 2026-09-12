

from typing import Optional
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskOut(TaskCreate):
    id: int