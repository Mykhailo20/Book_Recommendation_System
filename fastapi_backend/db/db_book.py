from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DbBook


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