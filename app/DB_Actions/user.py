from sqlalchemy.orm import Session
from app import models, schemas
from app.hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = models.User(
        full_name=request.full_name, username=request.username, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


