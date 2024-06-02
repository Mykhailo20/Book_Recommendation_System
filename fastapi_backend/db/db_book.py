from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DbBook, DbRating


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
    return query.all()


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