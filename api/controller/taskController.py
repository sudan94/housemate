from sqlalchemy.orm import Session

from models import taskModel, userModel, groupModel
from schemas import taskSchema
import datetime

def get_tasks(db: Session, skip: int =0, limit:  int = 100):
    return db.query(taskModel.Task).offset(skip).limit(limit).all()

def get_task(db : Session, task_id: int):
    return db.query(taskModel.Task).filter(taskModel.Task.id == task_id).first()

def create_task(db: Session, task:taskSchema.TaskCreate):
    db_task = taskModel.Task(title = task.title, description = task.description, frequency = task.frequency)
    print(task)
    db.add(db_task)
    db.commit()
    create_user_tasks(db=db,  date = task.date, task_id =  db_task.id, frequency = task.frequency, group_id = task.group_id)
    return db_task

def get_users(db: Session,task_id):
    return db.query(userModel.UserTask).join(userModel.User).filter(userModel.UserTask.task_id == task_id).all()

def create_user_tasks(db: Session,  date, task_id, frequency, group_id):
    users = db.query(userModel.User).join(groupModel.UserGroup).filter(groupModel.UserGroup.group_id == group_id).all()
    for j in range(len(users)):
        if j == 0:
            # due_date = datetime.strptime(date +" 00:00:00.0", "%m/%d/%y %H:%M:%S.%f")
            due_date = date
        else:
            start_date = datetime.datetime.strptime(date , "%Y-%m-%d")
            due_date = start_date + datetime.timedelta(days=frequency*j)
            print(due_date)
        user_id = users[j].id
        task = userModel.UserTask(task_id = task_id, user_id = user_id, due_date = due_date, group_id = group_id)
        db.add(task)
        db.commit()
        db.refresh(task)
    return True