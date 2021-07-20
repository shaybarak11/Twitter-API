from typing import List
from fastapi import APIRouter, Depends, status
from app import schemas, database
from sqlalchemy.orm import Session
from app.DB_Actions import retweets

router = APIRouter(
    prefix="/api"
)

get_db = database.get_db


@router.post('/tweets/{id}/retweet', status_code=status.HTTP_201_CREATED, tags=["Retweets"])
def create(id: int, request: schemas.ActionPost, db: Session = Depends(get_db)):
    return retweets.create(id, request, db)


@router.get('/retweets', response_model=List[schemas.ShowRetweet], tags=["Retweets"])
def all(db: Session = Depends(get_db)):
    return retweets.get_all(db)
