from sqlalchemy import Column,Integer,String,BOOLEAN
from src.utils.db import Base

class TaskModel(Base):
    __tablename__="user.tasks"

    id=Column(Integer,primary_key=True)
    title=Column(String)
    description=Column(String)
    is_completed=Column(BOOLEAN,default=False)

