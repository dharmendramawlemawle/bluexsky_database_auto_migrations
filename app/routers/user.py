from fastapi import FastAPI,Depends,status,Response,HTTPException, APIRouter
from sqlalchemy.orm import Session
import models as models
from schemas.user_schemas import User, ShowUser
from database import engine,get_db
from typing import List
from passlib.context import CryptContext


router = APIRouter(
    prefix="/v1",
    # dependencies=[Depends(get_bearer_header)],
    responses={404: {"description": "Not found"}},
    tags=["user"]
)


class Hash():
    def bcrypt(password:str):
        pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_cxt.hash(password)
    


@router.get('/user', status_code = 200, response_model = List[ShowUser])
def all_user(db:Session= Depends(get_db)):
    user = db.query(models.User).all()
    
    return user

@router.get('/user/{id}', status_code = 200, response_model = ShowUser)
def show_user(id: int,db:Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail = f'User with this id:{id} not found' )

    return user

@router.post('/user', status_code = 201, response_model = ShowUser)
def create_user(request: User, db:Session= Depends(get_db)):
    
    new_user = models.User(username=request.username, email = request.email,
    password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user