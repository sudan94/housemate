from sqlalchemy.orm import Session
from models import userModel,groupModel
from schemas import userSchema
from config import settings
from fastapi import Depends, HTTPException, status, Request
import requests
from jose import jwt

def get_user(db : Session, user_id: int):
    return db.query(userModel.User).filter(userModel.User.id == user_id).first()

def get_all_users(db : Session):
    return db.query(userModel.User).all()

def get_user_by_email(db: Session, email: str):
    return db.query(userModel.User).filter(userModel.User.email == email).first()

def create_user(db: Session, user: userSchema.UserCreate):
    db_user = userModel.User(email=user.email,name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_tasks(db: Session,user_id):
    return db.query(userModel.UserTask).join(userModel.User).filter(userModel.UserTask.user_id == user_id).all()

def auth_google(code):
    # token_url = "https://accounts.google.com/o/oauth2/token"
    # data = {
    #     "code": code,
    #     "client_id": settings.GOOGLE_CLIENT_ID,
    #     "client_secret": settings.GOOGLE_CLIENT_SECRET,
    #     "redirect_uri": settings.GOOGLE_REDIRECT_URI,
    #     "grant_type": "authorization_code",
    # }
    # response = requests.post(token_url, data=data)
    # access_token = response.json().get("access_token")
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {code}"})

    if user_info.status_code != 200:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    token = create_token(user_info.json())
    return token

def create_token(data: dict):
    payload = {
        "sub": data.get("id"),
        "name": data.get("name"),
        "email": data.get("email"),
        "picture": data.get("picture"),
    }
    return jwt.encode(payload, settings.GOOGLE_CLIENT_SECRET, algorithm="HS256")

def get_current_user(token: str):
    try:
        payload = jwt.decode(token, settings.GOOGLE_CLIENT_SECRET, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
        )

