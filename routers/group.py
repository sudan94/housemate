from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import groupSchema
from controller import groupController
from database import get_db

router = APIRouter(prefix="/group",
    tags=["Group"],
    responses={404: {"description": "Not found"}},
)

@router.get("", response_model=list[groupSchema.Group])
def read_group(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    group = groupController.get_groups(db, skip=skip, limit=limit)
    return group

@router.post("", response_model=groupSchema.Group)
def create_group(group: groupSchema.GroupCreate, db : Session= Depends(get_db)):
    return groupController.create_groups(db=db, group=group)

@router.post("/userGroup", response_model=groupSchema.GroupUserCreate)
def create_group(group: groupSchema.GroupUserCreate, db : Session= Depends(get_db)):
    return groupController.add_user_groups(db=db, group=group)