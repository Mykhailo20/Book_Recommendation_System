from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_user

router = APIRouter(prefix='/user', tags=['user'])


@router.get("/{username}")
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_username(db, username)