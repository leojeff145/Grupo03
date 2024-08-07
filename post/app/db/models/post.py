from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    img_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    #user_id = Column(Integer, ForeignKey('users.id'))
    

class PostBase(BaseModel):
    title: str
    body: str
    img_url: Optional[str] = None

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostInDBBase(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        

#Alias for the Pydantic model used in responses
Post = PostInDBBase