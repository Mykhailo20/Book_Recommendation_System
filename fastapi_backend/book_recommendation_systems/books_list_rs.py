import pandas as pd

from utils.recommend_books import get_books_recommendations_books_list_rs


def recommend_books(books_user_like_dict):

    # Read the necessary data
    books_df = pd.read_csv('../data/processed_data/Books.csv')
    ratings_df = pd.read_csv('../data/processed_data/Ratings.csv')
    books_user_like_df = pd.DataFrame.from_dict(books_user_like_dict)

    recommended_books = get_books_recommendations_books_list_rs(ratings_df, books_df, books_user_like_df)
    print(f"recommended_books = \n{recommended_books}")


if __name__ == "__main__":
    books_user_like = [
        '0590353403',   # Harry Potter and the Sorcerer's Stone (Book 1)
        '0439064872',   # Harry Potter and the Chamber of Secrets (Book 2)
        '0345350499'    # The Mists of Avalon
    ]

    books_user_like_titles = [
        "Harry Potter and the Sorcerer's Stone (Book 1)", 
        "Harry Potter and the Chamber of Secrets (Book 2)",
        "The Mists of Avalon"
    ]

    current_user_id = -1

    books_user_like_dict = {
        'user_id': [current_user_id for _ in range(len(books_user_like))],
        'isbn': books_user_like,
        'title': books_user_like_titles,
        'rating': [10, 9, 10]
    }

    recommend_books(books_user_like_dict)