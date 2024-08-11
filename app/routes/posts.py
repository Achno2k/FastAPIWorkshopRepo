from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. import utils, oauth2

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    
    print(current_user.id)
    new_post = models.Post(**(dict(post)), owner_id = current_user.id)
    db.add(new_post)
    db.commit()
    # db.refresh(new_post)

    return new_post
    

@router.put("/{id}", response_model=schemas.PostResponse, status_code=status.HTTP_202_ACCEPTED)
def update_posts(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    updated_post = db.query(models.Post).filter(models.Post.id == id)

    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This post does not exist. Please create one and try again")
    
    if updated_post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform this action")
    
    updated_post.update(dict(post), synchronize_session=False)
    db.commit()

    return updated_post.first()

@router.delete('/{id}')
def delete_post(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    
    deleted_post = db.query(models.Post).filter(models.Post.id == id)

    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    
    if deleted_post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform this action")

    deleted_post.delete(synchronize_session=False)  
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT) 