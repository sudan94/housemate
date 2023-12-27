from sqlalchemy.orm import Session
from models import userModel
from schemas import userSchema

def get_user(db : Session, user_id: int):
    return db.query(userModel.User).filter(userModel.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(userModel.User).filter(userModel.User.email == email).first()

def create_user(db: Session, user: userSchema.UserCreate):
    db_user = userModel.User(email=user.email,name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

