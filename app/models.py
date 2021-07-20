from sqlalchemy import Column, Integer, ForeignKey, DateTime, VARCHAR
from .database import Base
from datetime import datetime


class Tweet(Base):
    __tablename__ = 'tweets'

    post_id = Column(Integer, primary_key=True, autoincrement=True)
    text_content = Column(VARCHAR(500), nullable=False)
    username = Column(VARCHAR(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.now)


class Like(Base):
    __tablename__ = 'likes'

    username = Column(VARCHAR(50), primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey('tweets.post_id', ondelete="CASCADE"), primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)


class Retweet(Base):
    __tablename__ = 'retweets'

    username = Column(VARCHAR(50), primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey('tweets.post_id', ondelete="CASCADE"), primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)


class User(Base):
    __tablename__ = 'users'

    username = Column(VARCHAR(50), primary_key=True, nullable=False)
    full_name = Column(VARCHAR(50), nullable=False)
    password = Column(VARCHAR(100), nullable=False)




