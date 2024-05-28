from pydantic import BaseModel
from typing import Optional, List


class Like(BaseModel):
     id: int
     user_id: int
     post_id: int
     