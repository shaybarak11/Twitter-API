from typing import List
from fastapi import APIRouter, Depends, status
from app import schemas, database
from sqlalchemy.orm import Session
from app.DB_Actions import tweets

router = APIRouter(
    prefix="/api/tweets"
)

get_db = database.get_db


@router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowTweet], tags=["Tweets"])
def all(db: Session = Depends(get_db)):
    return tweets.get_all(db)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowTweet, tags=["Tweets"])
def create(request: schemas.TweetPost, db: Session = Depends(get_db)):
    return tweets.create(request, db)
