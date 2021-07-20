from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class TweetPost(BaseModel):
    text_content: str
    username: str


class ActionPost(BaseModel):
    username: str


class ShowTweet(BaseModel):
    post_id: int
    text_content: str
    username: str
    timestamp: datetime
    likes_count: int = 0
    retweets_count: int = 0

    class Config:
        orm_mode = True


class ShowRetweet(BaseModel):
    text_content: str
    retweet_username: str
    tweet_id: int
    tweet_username: str
    timestamp: datetime


class User(BaseModel):
    full_name: str
    username: str
    password: str


class ShowUser(BaseModel):
    full_name: str
    username: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
