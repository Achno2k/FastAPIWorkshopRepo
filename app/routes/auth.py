from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. import utils

router = APIRouter(
    prefix='/users',
    tags=['Authentication']
)

# @router.post('/login', status_code=status.HTTP_200_OK)
# def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
#     if utils.verify_password(user.password, )