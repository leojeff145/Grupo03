from app.db.models.post import Post, PostCreate, PostUpdate
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()

def create_post(db: Session, post: PostCreate):
    try:
        db_post = Post(**post.dict())
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post
    except SQLAlchemyError as e:
        logging.error(e)
        db.rollback()
        return None

def update_post(db: Session, post_id: int, post: PostUpdate):
    db_post = get_post(db, post_id)
    if db_post:
        for key, value in post.dict().items():
            setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = get_post(db, post_id)
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post
