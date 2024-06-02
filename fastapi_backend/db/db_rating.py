from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db.models import DbRating, DbBook
from routers.schemas import RatingBase


def create_rating(db: Session, request: RatingBase):
    try:
        rating = DbRating(
            isbn = request.isbn,
            user_id = request.user_id,
            rating = request.rating
        )
        db.add(rating)
        db.commit()
        db.refresh(rating)
        return rating

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An Integrity Error occurred while creating the rating: {e}"
        )
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"A SQLAlchemy Error occurred while creating the rating: {e}"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"An unexpected error occurred while creating the user: {str(e)}"
        )
    