from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db.models import DbUser, DbBook, DbRating
from db.db_utils import get_db_error_details, Hash
from routers.schemas import UserBase
from config.data_config import data, BOOK_DEFAULT_RATING
from book_recommendation_systems import one_book_rs, books_list_rs
from utils.data_converters import book_converter


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


def get_user_recommendations(db: Session, user_id: int, books_no: int, current_user_id: int):
    if current_user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="A user can get recommendations based on their saved books, but access to other users' recommendations is not allowed."
        )
    books_user_like = get_user_rated_books(db, user_id)
    
    # Get ratings for the books the user likes
    ratings = db.query(DbRating).filter(DbRating.user_id == user_id).all()
    # Create a dictionary mapping ISBN to rating
    rating_dict = {rating.isbn: rating.rating for rating in ratings}

    if len(books_user_like) == 1:

        book_user_like = books_user_like[0]
        rating = rating_dict[book_user_like.isbn]
        get_similar_books = rating > BOOK_DEFAULT_RATING
        # User likes rated book
        return one_book_rs.get_books_recommendations_1_book_rs(
            books_df=data['books_df'], 
            pivot_table=data['pivot_table'], 
            similarity_scores=data['similarity_scores'], 
            book_name=book_user_like.title,
            get_similar=get_similar_books,
            recommend_books_no=books_no
        )
        

    books_user_like_dict = {
        'user_id': [user_id for _ in range(len(books_user_like))],
        'isbn': [book.isbn for book in books_user_like],
        'title': [book.title for book in books_user_like],
        'rating': [rating_dict[book.isbn] for book in books_user_like]
    }

    recommended_books = books_list_rs.recommend_books(
        books_df=data['books_df'], 
        ratings_df=data['ratings_df'], 
        books_user_like_dict=books_user_like_dict,
        user_id=user_id,
        recommend_books_no=books_no
    )

    book_display_list = recommended_books.apply(lambda row: book_converter.convert_from_row(row), axis=1).tolist()

    return book_display_list