from sqlalchemy.orm import Session
from models import groupModel, userModel, taskModel
from schemas import groupSchema

def get_groups(db: Session, skip: int =0, limit:  int = 100, user_id: int = None):
    return db.query(groupModel.Group).join(groupModel.UserGroup).filter(groupModel.UserGroup.user_id == user_id).offset(skip).limit(limit).all()

def get_group(db: Session, group_id):
    return db.query(groupModel.Group).filter(groupModel.Group.id == group_id).first()

def create_groups(db: Session, group:groupSchema.GroupCreate):
    db_group = groupModel.Group(title = group.title, description = group.description)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def add_user_groups(db: Session, group:groupSchema.GroupUserCreate):
    db_user = db.query(userModel.User).filter(userModel.User.email == group.email).first()
    if db_user is None:
        db_user = userModel.User(email = group.email, is_active= False, name ='')
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    db_group = groupModel.UserGroup(group_id = group.group_id, user_id = db_user.id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_users(db: Session,group_id):
    return db.query(userModel.User).join(groupModel.UserGroup).filter(groupModel.UserGroup.group_id == group_id).all()

def get_tasks(db: Session, group_id):
    # return db.query(taskModel.Task).join(userModel.UserTask, taskModel.Task.id == userModel.UserTask.task_id, isouter=True).join(groupModel.UserGroup, groupModel.UserGroup.user_id == userModel.UserTask.user_id, isouter=True).filter(groupModel.UserGroup.group_id == group_id).all()
    # return db.query(userModel.User).join(groupModel.UserGroup).join(userModel.UserTask).join(taskModel.Task, isouter=True).filter(groupModel.UserGroup.group_id == group_id).all()
    # return db.query(userModel.User.email,taskModel.Task.title,userModel.UserTask.due_date, userModel.UserTask.is_completed).select_from(userModel.User).join(groupModel.UserGroup).join(userModel.UserTask).join(taskModel.Task).filter(groupModel.UserGroup.group_id == group_id).all()

    return db.query(userModel.User.email,taskModel.Task.title,userModel.UserTask.due_date, userModel.UserTask.is_completed).select_from(userModel.User).join(userModel.UserTask).join(taskModel.Task).filter(userModel.UserTask.group_id == group_id).all()