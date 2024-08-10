from fastapi import Response, status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. import utils
from .. import oauth2

router = APIRouter(
    prefix='/users',
    tags=['Authentication']
)

@router.post('/login', status_code=status.HTTP_200_OK, response_model=schemas.AccessToken)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email not found. Please create a new account")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials. Please try again")

    access_token = oauth2.create_access_token(
        {"user_id": user.id}
    )
    return {"access_token": access_token, "token_type": "bearer"}




    