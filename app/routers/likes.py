from fastapi import APIRouter, Depends, status
from app import schemas, database
from sqlalchemy.orm import Session
from app.DB_Actions import likes

router = APIRouter(
    prefix="/api/tweets"
)

get_db = database.get_db


@router.post('/{id}/likes', status_code=status.HTTP_201_CREATED, tags=["Likes"])
def create(id: int, request: schemas.ActionPost, db: Session = Depends(get_db)):
    return likes.create(id, request, db)
