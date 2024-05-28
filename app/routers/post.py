from fastapi import FastAPI,Depends,status,Response,HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas.post_schema import ShowPost, Post, UpdatePost
import models as models
from database import engine,get_db
from typing import List

router = APIRouter(
    prefix="/v1",
    # dependencies=[Depends(get_bearer_header)],
    responses={404: {"description": "Not found"}},
    tags=["posts"]
)




@router.get('/post',status_code=200, response_model = List[ShowPost])
def all_posts(db:Session= Depends(get_db)):
    post = db.query(models.Posts).all()
    return post

@router.get('/post/{id}',status_code=200, response_model = ShowPost)
def show(id: int, response:Response, db:Session= Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'Blog for this id:{id} not found' )
    return post


@router.post('/post/', status_code = 201)
def create(post:Post, db:Session= Depends(get_db)):
    author = db.query(models.User).filter(models.User.id == post.author_id).first()
    if not author:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'Author not found for id:{post.author_id} enter valid author')
    else:
        new_post = models.Posts(
                    title= post.title,
                    content= post.content,
                    author_id= author.id
            )
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post


@router.put('/post/{id}',status_code=202, response_model = ShowPost)
def update(id,request:UpdatePost,db:Session= Depends(get_db)):
    
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'Post for this id:{id} not found' )
    else:
        post.title= request.title
        post.content =request.content
        db.commit()
        return post
    

@router.delete('/post/{id}', status_code=204)
def destroy(id,db:Session= Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id)
    if not post.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f'Blog for this id:{id} not found' )
    post.delete(synchronize_session=False)
    db.commit()
    return {"status":204, "message":"successfully deleted"}
