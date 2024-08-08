from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. import utils

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.password = utils.hash_password(user.password)

    new_user = models.User(**(dict(user)))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user




    






