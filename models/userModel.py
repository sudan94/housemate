from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
# from enum import Enum, unique
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)


class UserTask(Base):
    __tablename__ = "usertask"

    id= Column(Integer,primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_id = Column(Integer, ForeignKey("task.id"))
    status = Column(Enum("Due", "Pending", "Completed", name="ValueTypes"), default= "Due")
