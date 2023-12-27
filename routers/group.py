from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import groupSchema
from crud import crud_group
from database import get_db

router = APIRouter()

@router.get("/group", response_model=list[groupSchema.Group])
def read_group(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    group = crud_group.get_groups(db, skip=skip, limit=limit)
    return group

@router.post("/group", response_model=groupSchema.Group)
def create_group(group: groupSchema.GroupCreate, db : Session= Depends(get_db)):
    return crud_group.create_groups(db=db, group=group)

@router.post("/userGroup", response_model=groupSchema.GroupUserCreate)
def create_group(group: groupSchema.GroupUserCreate, db : Session= Depends(get_db)):
    return crud_group.add_user_groups(db=db, group=group)