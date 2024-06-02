from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_rating
from routers.schemas import RatingBase, RatingDisplay, UserAuth
from utils.auth.oauth2 import get_current_user


router = APIRouter(prefix='/rating', tags=['rating'])


@router.post("", response_model=RatingDisplay)
def create_rating(request: RatingBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_rating.create_rating(db, request, current_user.user_id)