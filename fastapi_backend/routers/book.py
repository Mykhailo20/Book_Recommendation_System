from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_book
from routers.schemas import BookDisplay, RatingDisplay
from config.data_config import ONE_BOOK_RS_RECOMMEND_BOOKS_NO



router = APIRouter(prefix='/book', tags=['book'])


@router.get('/most_popular', response_model=list[BookDisplay])
def get_most_popular_books(db: Session = Depends(get_db)):
    return db_book.get_most_popular_books(db)


@router.get("/similar/{title}", response_model=list[BookDisplay])
def get_similar_books(
    title: str = Path(..., title='The title of the book for which similar books will be returned', max_length=300),
    books_no: int | None = Query(default=ONE_BOOK_RS_RECOMMEND_BOOKS_NO, ge=1, lt=50),
    db: Session = Depends(get_db)
):
    return db_book.get_similar_books(db, title, books_no)


@router.get('/search', response_model=list[BookDisplay])
def search_books(
    title: str | None = Query(None, title='The title of the book to search for'),
    author: str | None = Query(None, title='The author of the book to search for'),
    db: Session = Depends(get_db)
):
    return db_book.search_books(db, title, author)
    


@router.get('/{isbn}', response_model=BookDisplay)
def get_book_by_isbn(
    isbn: str = Path(..., title='The isbn of the book to get', min_length=10, max_length=10),
    db: Session = Depends(get_db)
):
    return db_book.get_book_by_isbn(db, isbn)


@router.get('/{isbn}/ratings', response_model=list[RatingDisplay], tags=['book', 'rating'])
def get_book_ratings(
    isbn: str = Path(..., title='The isbn of the book ratings of which to get', min_length=10, max_length=10),
    db: Session = Depends(get_db)
):
    return db_book.get_book_ratings(db, isbn)

