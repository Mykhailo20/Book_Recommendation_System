import pandas as pd
from routers.schemas import BookDisplay


def convert_from_row(row: pd.Series):
    return BookDisplay(
        isbn = row['isbn'],
        title = row['title'],
        author = row['author'],
        publication_year = row['publication_year'],
        publisher = row['publisher'],
        image_url = row['image_url']
    )