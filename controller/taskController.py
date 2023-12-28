from sqlalchemy.orm import Session

from models import taskModel
from schemas import taskSchema

def get_tasks(db: Session, skip: int =0, limit:  int = 100):
    return db.query(taskModel.Task).offset(skip).limit(limit).all()

def get_task(db : Session, task_id: int):
    return db.query(taskModel.Task).filter(taskModel.Task.id == task_id).first()

def create_task(db: Session, task:taskSchema.TaskCreate):
    db_task = taskModel.Task(title = task.title, description = task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
