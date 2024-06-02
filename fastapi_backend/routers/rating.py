from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_rating
from routers.schemas import RatingBase, RatingDisplay


router = APIRouter(prefix='/rating', tags=['rating'])


@router.post("", response_model=RatingDisplay)
def create_rating(request: RatingBase, db: Session = Depends(get_db)):
    return db_rating.create_rating(db, request)