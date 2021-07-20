from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status


def check_if_like_already_exist(id: int, username: str, db: Session):
    like = db.query(models.Like).filter_by(post_id=id, username=username).first()
    if like:
        return like
    else:
        return False


def create(id: int, request: schemas.ActionPost, db: Session):
    post = db.query(models.Tweet).filter_by(post_id=id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    like = check_if_like_already_exist(id, request.username, db)
    if like:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"{request.username} already liked this post id {id}")

    new_like = models.Like(username=request.username, post_id=id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like
