from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, status, APIRouter, Request
import python_jwt as jwt, jwcrypto.jwk as jwk, datetime
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
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        header, claims = jwt.verify_jwt(credentials.credentials, jwk.JWK.from_password(settings.GOOGLE_CLIENT_SECRET), ['HS256'])
        return claims
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
        )

def get_user_id(token: str, db):
    header, claims = jwt.verify_jwt(token, jwk.JWK.from_password(settings.GOOGLE_CLIENT_SECRET), ['HS256'])
    user = db.query(userModel.User).filter(userModel.User.email == claims['email']).first()
    return user.id
