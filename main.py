from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas import User, Item
from fastapi_sqlalchemy import DBSessionMiddleware, db

from app.models import User, Item
from app.database import Sessionlocal, engine

from app.schemas import User, Item



app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

 #to avoid csrftokenError



# Dependency
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/Item/", response_model=Item)
def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item        

@app.get("/Items", response_model=Item)
def read_Item(token: str = Depends(oauth2_scheme)):
    return {Item.name: Item.description
            }