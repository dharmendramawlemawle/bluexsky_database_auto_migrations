from fastapi import FastAPI
import models as models
from database import engine,Base 
from routers import post,user

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)