from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm.session import Session

from db.database import get_db
from db import db_book
from routers.schemas import BookDisplay, RatingDisplay
from config.data_config import ONE_BOOK_RS_RECOMMEND_BOOKS_NO, POPULARITY_RS_RECOMMEND_BOOKS_NO, AUTHORS_NO



router = APIRouter(prefix='/book', tags=['book'])


@router.get('/most_popular', response_model=list[BookDisplay])
def get_most_popular_books(
    db: Session = Depends(get_db), 
    books_no: int | None = Query(default=POPULARITY_RS_RECOMMEND_BOOKS_NO, ge=1)
):
    return db_book.get_most_popular_books(db, books_no)


@router.get("/similar", response_model=list[BookDisplay])
def get_similar_books(
    isbn: str | None = Query(None, isbn='The isbn of the book for which similar books will be returned', min_length=10, max_length=10),
    title: str | None = Query(None, title='The title of the book for which similar books will be returned'),
    books_no: int | None = Query(default=ONE_BOOK_RS_RECOMMEND_BOOKS_NO, ge=1, lt=50),
    db: Session = Depends(get_db)
):
    return db_book.get_similar_books(db, books_no, isbn, title)


@router.get("/similar/all_titles")
def get_1_book_rs_titles(db: Session = Depends(get_db)):
    return db_book.get_1_book_rs_all_titles(db)


@router.get('/search', response_model=list[BookDisplay])
def search_books(
    title: str | None = Query(None, title='The title of the book to search for'),
    author: str | None = Query(None, title='The author of the book to search for'),
    db: Session = Depends(get_db)
):
    return db_book.search_books(db, title, author)
    

@router.get('/authors')
async def get_authors(db: Session = Depends(get_db)):
    return await db_book.get_book_authors(db)


@router.get('/authors_most_books')
async def get_authors_with_most_books(
    db: Session = Depends(get_db),
    books_no: int | None = Query(default=AUTHORS_NO, ge=1)
):
    return await db_book.get_authors_with_most_books(db, books_no)


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

