from pydantic import BaseModel
from models import userModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    frequency : int | None = None
    date : str | None = None


class TaskCreate(TaskBase):
    starting_user : int
    group_id : int

class TaskUser(BaseModel):
    task_id : int

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
