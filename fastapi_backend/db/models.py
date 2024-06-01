from sqlalchemy import Column, Integer, String

from .database import Base


class DbUser(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(64))
    