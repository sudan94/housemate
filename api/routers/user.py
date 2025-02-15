from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from schemas import userSchema
from controller import userController
from utils import auth
from database import get_db
import python_jwt as jwt, jwcrypto.jwk as jwk
from config import settings

router = APIRouter(    prefix="/user",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{user_id}", response_model=userSchema.User)
def get_user_by_id(user_id : int, db: Session = Depends(get_db)):
    db_user = userController.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not Found")
    return db_user

@router.get("", response_model=list[userSchema.User])
def get_users(db: Session = Depends(get_db)):
    db_user = userController.get_all_users(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not Found")
    return db_user

@router.post("", response_model=userSchema.User)
def create_user(user: userSchema.UserCreate, db: Session =Depends(get_db)):
    db_user = userController.get_user_by_email(db, email=user.email)
    if db_user:
        userController.auth_google(token = user.token)
    return userController.create_user(db=db, user=user)

@router.get("/tasks/{user_id}")
def get_user_by_groups(user_id : int, db: Session = Depends(get_db), current_user: userSchema.UserToken = Depends(auth.get_current_user)):
    db_user = userController.get_tasks(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Tasks not Found")
    return db_user

@router.post("/login")
async def login(request: Request, db: Session = Depends(get_db)):
    token = await request.json()
    code = token['code']
    is_valid = userController.auth_google(code = code)
    if not is_valid:
        raise HTTPException(status_code=401, detail="Invalid token")
    header, claims = jwt.verify_jwt(is_valid, jwk.JWK.from_password(settings.GOOGLE_CLIENT_SECRET), ['HS256'])
    return is_valid


# @router.delete("/{user_id}", response_model=userSchema.User)
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = userController.delete_user(db, id = user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not Found")
#     return db_user
