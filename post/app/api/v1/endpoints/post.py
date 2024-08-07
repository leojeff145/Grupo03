from app.db.models.post import Post, PostCreate, PostUpdate
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services import post_service

router = APIRouter()

@router.get('/posts/all/', response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = post_service.get_posts(db, skip=skip, limit=limit)
    return posts

@router.post('/posts/create/', response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return post_service.create_post(db = db, post = post)

@router.get('/posts/{post_id}', response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = post_service.get_post(db, post_id = post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    return db_post

@router.put('/posts/update/{post_id}', response_model=Post)
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    db_post = post_service.update_post(db, post_id = post_id, post = post)
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    return db_post

@router.delete('/posts/delete/{post_id}', response_model=Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = post_service.delete_post(db, post_id = post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    return db_post