from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    class Config():
        orm_mode = True


class BookDisplay(BaseModel):
    # isbn: str
    title: str
    author: str
    publication_year: int
    publisher: str
    image_url: str
    class Config():
        orm_mode = True