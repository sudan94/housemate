from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import taskSchema
from controller import taskController
from database import get_db

router = APIRouter(prefix="/tasks",
    tags=["Tasks"],
    responses={404: {"description": "Not found"}},
)

@router.get("", response_model=list[taskSchema.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = taskController.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.post("", response_model=taskSchema.Task)
def create_task(task: taskSchema.TaskCreate, db : Session= Depends(get_db)):
    return taskController.create_task(db=db, task=task)