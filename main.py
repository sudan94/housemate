from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import taskModel, userModel, groupModel
from routers import task, user, group
from database import SessionLocal
import requests
from dotenv import load_dotenv
load_dotenv()
import os

taskModel.Base.metadata.create_all(bind= engine)
userModel.Base.metadata.create_all(bind= engine)
groupModel.Base.metadata.create_all(bind= engine)


app =FastAPI()

origins = [
    "*",
]

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(task.router)
app.include_router(group.router)




