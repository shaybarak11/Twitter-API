from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB_NAME = "twitter"

SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
print(SQLALCHEMY_DATABASE_URI)


engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
