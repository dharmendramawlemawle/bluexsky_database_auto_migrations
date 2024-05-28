from pydantic import BaseModel
from typing import Optional, List


class Comment(BaseModel):
     id: int
     content: str
     post_id: str
     author_id: int