from pydantic import BaseModel
from typing import Optional, List
from schemas.post_schema import Post

class User(BaseModel):

     username: str
     email: str
     password : str  
     
class ShowUser(BaseModel):
     id :int
     status: str = "success"
     username: str
     email: str
     status: str = "Active" 
     post : List[Post] = []      # name of relation ship which we made
     class Config:
          orm_mode = True