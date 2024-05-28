from pydantic import BaseModel
from typing import Optional, List




     
class Post(BaseModel):
     title: str
     content: str
     author_id: int

class User(BaseModel):
     id:int
     username: str
     
     
class Comment(BaseModel):
     content: str

class Category(BaseModel):
     name: str

class Like(BaseModel):
     user: User
     
class ShowPost(BaseModel):
     id: int
     title: str
     content: str
     author : User
     # comment: Comment
     # category:Category
     # like: Like
     
          
class UpdatePost(BaseModel):
     title: str
     content: str