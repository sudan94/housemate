from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import userSchema
from crud import crud_user
from database import get_db

router = APIRouter()

@router.get("/user/{user_id}", response_model=userSchema.User)
def get_user(user_id : int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not Found")
    return db_user

@router.post("/users", response_model=userSchema.User)
def create_user(user: userSchema.UserCreate, db: Session =Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db=db, user=user)

