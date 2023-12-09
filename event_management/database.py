from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

USER_DB=os.getenv("DBUSER")
PASSWORD_DB=os.getenv("DBPASSWORD")
HOST_DB=os.getenv("DBHOST")
NAME_DB=os.getenv("DBNAME")

SQLALCHEMY_DATABASE_URL=f"postgresql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}/{NAME_DB}"

engine=create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()