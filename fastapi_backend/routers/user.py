from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_user
from routers.schemas import UserBase, UserDisplay, BookDisplay

router = APIRouter(prefix='/user', tags=['user'])


@router.post("", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get("/all", response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)
    

@router.get("/{username}", response_model=UserDisplay)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_username(db, username)


@router.get("/{user_id}/rated_books", response_model=list[BookDisplay], tags=['user', 'rating'])
def get_user_rated_books(user_id: int, db: Session=Depends(get_db)):
    return db_user.get_user_rated_books(db, user_id)