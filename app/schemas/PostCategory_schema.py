from pydantic import BaseModel
from typing import Optional, List


class PostCategory(BaseModel):
     id: int
     category_id: int
     post_id: int
     