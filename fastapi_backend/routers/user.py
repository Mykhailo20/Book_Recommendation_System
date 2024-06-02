from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_user
from routers.schemas import UserBase, UserDisplay, BookDisplay, UserAuth
from utils.auth.oauth2 import get_current_user
from config.data_config import BOOKS_LIST_RS_RECOMMEND_BOOKS_NO

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
def get_user_rated_books(user_id: int, db: Session=Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_user.get_user_rated_books(db, user_id)


@router.get("/{user_id}/recommendations", tags=['user', 'book'])
def get_user_recommendations(
    user_id: int, 
    db: Session=Depends(get_db),
    books_no: int | None = Query(default=BOOKS_LIST_RS_RECOMMEND_BOOKS_NO, ge=1, lt=50),
    current_user: UserAuth = Depends(get_current_user)
):
    return db_user.get_user_recommendations(db, user_id, books_no, current_user.user_id)