from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from .database import Base


class DbUser(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(64))
    ratings = relationship('DbRating', back_populates='author')


class DbBook(Base):
    __tablename__ = 'book'
    isbn = Column(String(10), primary_key=True)
    title = Column(String(300))
    author = Column(String(255))
    publication_year = Column(Integer)
    publisher = Column(String(255))
    image_url = Column(String(2048))
    ratings = relationship('DbRating', back_populates='book')



class DbRating(Base):
    __tablename__ = 'rating'
    isbn = Column(String(10), ForeignKey('book.isbn'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    rating = Column(Integer, CheckConstraint('rating >= 0 AND rating <= 10', name='rating_rating_check'))
    author = relationship('DbUser', back_populates='ratings')
    book = relationship('DbBook', back_populates='ratings')
    