from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, status, APIRouter, Request
from jose import jwt
from config import settings
from models import userModel
from sqlalchemy.orm import Session
from database import get_db


security = HTTPBearer()

router = APIRouter(prefix="",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

@router.get("/active")
def get_current_user(credentials: HTTPAuthorizationCredentials= Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, settings.GOOGLE_CLIENT_SECRET, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
        )
def get_user_id(token : str, db):
    payload = jwt.decode(token, settings.GOOGLE_CLIENT_SECRET, algorithms=["HS256"])
    user = db.query(userModel.User).filter(userModel.User.email == payload['email']).first()
    return user.id
