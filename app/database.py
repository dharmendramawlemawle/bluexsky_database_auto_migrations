import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sqll lite database
DATABASE_URL = os.getenv('DATABASE_URL')
# DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, echo = False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


