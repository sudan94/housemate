from sqlalchemy.orm import Session

from models import taskModel, userModel
from schemas import taskSchema

def get_tasks(db: Session, skip: int =0, limit:  int = 100):
    return db.query(taskModel.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task:taskSchema.TaskCreate):
    db_task = taskModel.Task(title = task.title, description = task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    # create_user_task(db_task)
    return db_task

# def create_user_task(db: Session, data:taskModel):
#     db_task = userModel.UserTask(task_id = data.id)
#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)
#     return db_task