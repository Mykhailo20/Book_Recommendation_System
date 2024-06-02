from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db.models import DbUser, DbBook, DbRating
from db.db_utils import get_db_error_details, Hash
from routers.schemas import UserBase


def create_user(db: Session, request: UserBase):
    try:
        user = DbUser(
            username=request.username,
            email=request.email,
            password=Hash.bcrypt(request.password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError as e:
        db.rollback()
        detail = get_db_error_details(request, e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )
    
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An error occurred while creating the user: {e}"
        )
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An unexpected error occurred while creating the user: {str(e)}"
        )
    

def get_all_users(db: Session):
    return db.query(DbUser).all()


def check_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id '{user_id}' not found."
        )


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username '{username}' not found."
        )
    return user


def get_user_rated_books(db: Session, user_id: int):
    check_user(db, user_id)
    books = db.query(DbBook).join(DbRating, DbBook.isbn == DbRating.isbn).filter(DbRating.user_id == user_id).all()
    return books
