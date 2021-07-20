from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status
from datetime import datetime


def check_if_retweet_already_exist(id: int, username: str, db: Session):
    retweet = db.query(models.Retweet).filter_by(post_id=id, username=username).first()
    if retweet:
        return retweet
    else:
        return False


def create(id: int, request: schemas.ActionPost, db: Session):
    post = db.query(models.Tweet).filter_by(post_id=id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    retweet = check_if_retweet_already_exist(id, request.username, db)
    if retweet:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"{request.username} already retweeted this post id {id}")

    new_retweet = models.Retweet(username=request.username, post_id=id)
    db.add(new_retweet)
    db.commit()
    db.refresh(new_retweet)
    return new_retweet


def get_all(db: Session):
    retweets = db.query(models.Retweet).all()
    if not retweets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No retweets found")
    retweets_list = []
    for retweet in retweets:
        tweet = db.query(models.Tweet).filter_by(post_id=retweet.post_id).first()
        retweet_data = {
            "text_content": tweet.text_content,
            "retweet_username": retweet.username,
            "tweet_id": retweet.post_id,
            "tweet_username": tweet.username,
            "timestamp": datetime.isoformat(retweet.timestamp)
        }
        retweets_list.append(retweet_data)
    return retweets_list
