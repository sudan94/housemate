from sqlalchemy import Column, Integer, String, Boolean, Date

from database import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer,primary_key=True, index=True)
    title = Column(String,index=True)
    description = Column(String, index=True)
    frequency = Column(Integer, index = True)
    date = Column(Date, index=True)
