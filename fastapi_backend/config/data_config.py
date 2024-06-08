import pickle

import pandas as pd
from contextlib import asynccontextmanager

from config.files_config import BOOKS_DATA_FILEPATH, RATINGS_DATA_FILEPATH, PIVOT_TABLE_FILEPATH, SIMILARITY_SCORES_FILEPATH, BOOKS_POPULARITY_DATA_FILEPATH


POPULARITY_RS_RECOMMEND_BOOKS_NO = 10
ONE_BOOK_RS_RECOMMEND_BOOKS_NO = 5
BOOKS_LIST_RS_RECOMMEND_BOOKS_NO = 10
AUTHORS_NO = 50
BOOK_DEFAULT_RATING = 5

DB_INTEGRITY_ERROR_PATTERNS = {
    "username_unique": {
        "pattern": r'Key \(username\)=\((.+?)\) already exists',
        "answer_func": lambda username: f"User with username '{username}' already exists."
    },
    "email_unique": {
        "pattern": r'Key \(email\)=\((.+?)\) already exists',
        "answer_func": lambda email: f"User with email '{email}' already exists."
    },
    "email_check": {
        "pattern": r'relation \"user\" violates check constraint \"user_email_check\"',
        "answer_func": lambda email: f"The email '{email}' is not valid."
    }
}

RS_INTEGRITY_ERROR_PATTERNS = {
    "title_not_found": {
        "pattern": r"Book '(.+?)' not found in the dataset.",
        "answer_func": lambda title: f"Book with title '{title}' not found."
    }
}

data = {

}


async def load_data(
        books_data_filepath:str,
        ratings_data_filepath:str,
        pivot_table_filepath:str,
        similarity_scores_filepath:str,
        books_popularity_data_filepath:str
    ):
    data["books_df"] = pd.read_csv(books_data_filepath)
    data["ratings_df"] = pd.read_csv(ratings_data_filepath)
    data["pivot_table"] = pickle.load(open(pivot_table_filepath, 'rb'))
    data["similarity_scores"] = pickle.load(open(similarity_scores_filepath, 'rb'))
    data["books_popularity_df"] = pd.read_csv(books_popularity_data_filepath)


@asynccontextmanager
async def lifespan(app):
    # startup
    await load_data(
        books_data_filepath=BOOKS_DATA_FILEPATH,
        ratings_data_filepath=RATINGS_DATA_FILEPATH,
        pivot_table_filepath=PIVOT_TABLE_FILEPATH,
        similarity_scores_filepath=SIMILARITY_SCORES_FILEPATH,
        books_popularity_data_filepath=BOOKS_POPULARITY_DATA_FILEPATH
    )

    yield

    # shutdown
    data.clear()