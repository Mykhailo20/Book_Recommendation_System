from fastapi import APIRouter, Depends, Path, Query, HTTPException, status
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_book
from config.data_config import data, ONE_BOOK_RS_RECOMMEND_BOOKS_NO
from book_recommendation_systems import popularity_rs, one_book_rs
from utils.data_converters import book_converter
from utils import get_error_details


router = APIRouter(prefix='/book', tags=['book'])


@router.get('/most_popular')
def get_most_popular_books():
    
    recommended_books = popularity_rs.recommend_books(books_df=data['books_df'], ratings_df=data['ratings_df'])

    # Apply the conversion function to each row
    book_display_list = recommended_books.apply(lambda row: book_converter.convert_from_row(row), axis=1).tolist()

    return {
        "data": book_display_list
    }


@router.get("/similar/{title}")
def get_similar_books(
    title: str = Path(..., title='The title of the book for which similar books will be returned', max_length=300),
    books_no: int | None = Query(default=ONE_BOOK_RS_RECOMMEND_BOOKS_NO, ge=1, lt=50)
):
    try:
        similar_books = one_book_rs.get_books_recommendations_1_book_rs(
            books_df=data['books_df'], 
            pivot_table=data['pivot_table'], 
            similarity_scores=data['similarity_scores'], 
            book_name=title,
            recommend_books_no=books_no
        )

        return similar_books
    
    except ValueError as e:
        detail = get_error_details.get_rs_error_details(request_value=title, error=e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )


@router.get('/{isbn}')
def get_book_by_isbn(
    isbn: str = Path(..., title='The isbn of the book to get', min_length=10, max_length=10),
    db: Session = Depends(get_db)
):
    return db_book.get_book_by_isbn(db, isbn)

