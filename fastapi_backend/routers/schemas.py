from pydantic import BaseModel


# Book inside RatingDisplay
class Book(BaseModel):
    isbn: str
    title: str
    author: str
    image_url: str
    class Config():
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


# Rating inside UserDisplay
class Rating(BaseModel):
    rating: int
    book: Book
    class Config():
        orm_mode = True


class UserDisplay(BaseModel):
    user_id: str
    username: str
    # ratings: list[Rating]
    class Config():
        orm_mode = True


class BookDisplay(BaseModel):
    isbn: str
    title: str
    author: str
    publication_year: int
    publisher: str
    image_url: str
    class Config():
        orm_mode = True


class RatingBase(BaseModel):
    isbn: str
    user_id: int
    rating: int


# User inside RatingDisplay
class User(BaseModel):
    username: str
    class Config():
        orm_mode = True


class RatingDisplay(BaseModel):
    isbn: str
    user_id: int
    rating: int
    author: User
    book: Book
    class Config():
        orm_mode = True