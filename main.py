from fastapi import FastAPI
import uvicorn
from app import models
from app.database import engine
from app.routers import tweets, likes, retweets

app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(tweets.router)
app.include_router(likes.router)
app.include_router(retweets.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")

