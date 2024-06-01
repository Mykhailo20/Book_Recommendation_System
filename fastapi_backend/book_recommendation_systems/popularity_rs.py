import pandas as pd

from utils.metrics import calc_weighted_rating

MIN_BOOK_RATINGS_NO_PB = 100   # The minimum number of ratings for a single book to be used to build a Popularity Based Recommender System
DEFAULT_RATING = 5   # The neutral rating of the book


def recommend_books(books_df: pd.DataFrame, ratings_df: pd.DataFrame, recommend_books_no:int = 10) -> pd.DataFrame:
    rating_book_df = ratings_df.merge(books_df, on='isbn')
    book_rated_df = (
        rating_book_df
        .drop('image_url', axis=1)
        .groupby('title')
        ['rating']
        .agg(['count', 'mean'])
        .reset_index()
        .rename(
            columns={
                'count': 'ratings_no',
                'mean': 'avg_rating'
            }
        )
    )
    book_rated_df = (
        book_rated_df
        [book_rated_df['ratings_no'] >= MIN_BOOK_RATINGS_NO_PB]
        .sort_values(by='avg_rating', ascending=False)
    )

    book_rated_df['weighted_rating'] = (
        book_rated_df
        .apply(
                lambda x: calc_weighted_rating(x, 'avg_rating', 'ratings_no', MIN_BOOK_RATINGS_NO_PB, DEFAULT_RATING), 
            axis=1)
    )

    return book_rated_df.sort_values(by='weighted_rating', ascending=False).head(recommend_books_no)


if __name__ == "__main__":
    books_df = pd.read_csv('../data/db_data/Books.csv')
    ratings_df = pd.read_csv('../data/db_data/Ratings.csv')
    recommended_books = recommend_books(books_df, ratings_df)
    print(f"recommended_books = \n{recommended_books}")