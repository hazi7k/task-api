# Imports
from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field

# Classes
class TaskBase(SQLModel): 
    title: str = Field(min_length = 1, max_length = 120)
    description: Optional[str] = Field(default = None, max_length = 1000)
    is_done: bool = False

class Task(TaskBase, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    description: Optional[str] = Field(default=None, max_length=1000)
    is_done: Optional[bool] = None

