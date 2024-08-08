from fastapi import FastAPI
from .database import engine
from . import models
from .routes import users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get('/')
def home_route():
    return {"message": "Hello World"}

