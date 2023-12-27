from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import taskSchema
from crud import crud_task
from database import get_db

router = APIRouter()

@router.get("/tasks/", response_model=list[taskSchema.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud_task.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.post("/task", response_model=taskSchema.Task)
def create_task(task: taskSchema.TaskCreate, db : Session= Depends(get_db)):
    return crud_task.create_task(db=db, task=task)