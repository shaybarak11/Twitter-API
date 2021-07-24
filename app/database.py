from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


USERNAME = os.getenv("USERNAME", "root")
PASSWORD = os.getenv("PASSWORD", "password")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = os.getenv("PORT", 3306)
DB_NAME = os.getenv("DB_NAME", "twitter")

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
