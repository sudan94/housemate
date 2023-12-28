from sqlalchemy.orm import Session

from models import groupModel, userModel
from schemas import groupSchema

def get_groups(db: Session, skip: int =0, limit:  int = 100):
    return db.query(groupModel.Group).offset(skip).limit(limit).all()

def get_group(db: Session, group_id):
    return db.query(groupModel.Group).filter(groupModel.Group.id == group_id).first()

def create_groups(db: Session, group:groupSchema.GroupCreate):
    db_group = groupModel.Group(title = group.title, description = group.description)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def add_user_groups(db: Session, group:groupSchema.GroupUserCreate):
    db_group = groupModel.UserGroup(group_id = group.group_id, user_id = group.user_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_users(db: Session,group_id):
    return db.query(groupModel.UserGroup).join(userModel.User).filter(groupModel.UserGroup.group_id == group_id).all()
