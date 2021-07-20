from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status
from datetime import datetime


def get_all(db: Session):
    tweets = db.query(models.Tweet).all()
    if not tweets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No tweets found")

    tweets_list = []
    for tweet in tweets:
        likes = db.query(models.Like).filter_by(post_id=tweet.post_id).count()
        retweet = db.query(models.Retweet).filter_by(post_id=tweet.post_id).count()
        tweet_data = {
            "post_id": tweet.post_id,
            "text_content": tweet.text_content,
            "username": tweet.username,
            "timestamp": datetime.isoformat(tweet.timestamp),
            "likes_count": likes,
            "retweets_count": retweet
        }
        tweets_list.append(tweet_data)
    return tweets_list


def create(request: schemas.TweetPost, db: Session):
    new_tweet = models.Tweet(username=request.username, text_content=request.text_content)
    db.add(new_tweet)
    db.commit()
    db.refresh(new_tweet)
    return new_tweet

