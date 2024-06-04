from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DbBook, DbRating
from config.data_config import data
from book_recommendation_systems import popularity_rs, one_book_rs

from utils.data_converters import book_converter
from utils import get_error_details


def get_book_by_isbn(db: Session, isbn: str):
    book = db.query(DbBook).filter(DbBook.isbn == isbn).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with isbn '{isbn}' not found."
        )
    return book


def search_books(db: Session, title: str|None = None, author: str|None = None):
    query = db.query(DbBook)
    if title:
        query = query.filter(DbBook.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(DbBook.author.ilike(f"%{author}%"))
    books = query.all()
    if not books:
        raise HTTPException(
            status_code=404,
            detail="No books found matching the search criteria."
        )
    return books


def check_book(db: Session, book_isbn: str):
    book = db.query(DbBook).filter(DbBook.isbn == book_isbn).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with isbn '{book_isbn}' not found."
        )
    
    
def get_book_ratings(db: Session, book_isbn: str):
    check_book(db, book_isbn)
    ratings = db.query(DbRating).filter(DbRating.isbn == book_isbn).all()
    return ratings


def get_most_popular_books(db: Session):
    recommended_books = popularity_rs.recommend_books(books_df=data['books_df'], ratings_df=data['ratings_df'])
    # Apply the conversion function to each row
    book_display_list = recommended_books.apply(lambda row: book_converter.convert_from_row(row), axis=1).tolist()
    return book_display_list


def get_similar_books(db: Session, title: str, books_no: int):
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