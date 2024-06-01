import pickle

import pandas as pd

from utils.recommend_books import get_books_recommendations_1_book_rs
# from config.data_config import ONE_BOOK_RS_RECOMMEND_BOOKS_NO


def recommend_books(book_name):
    # Read the necessary data
    books_df = pd.read_csv('../data/db_data/Books.csv')
    pivot_table = pickle.load(open('../artifacts/pivot_table.pkl', 'rb'))
    similarity_scores = pickle.load(open('../artifacts/similarity_scores.pkl', 'rb'))

    try:
        res = (
            get_books_recommendations_1_book_rs(books_df=books_df, 
                                                book_name=book_name, 
                                                pivot_table=pivot_table, 
                                                similarity_scores=similarity_scores,
                                                recommend_books_no=5 # ONE_BOOK_RS_RECOMMEND_BOOKS_NO
            )
        )
        print(f"book_name: {book_name}")
        print(f"recommended_books: ")
        for index, book_list in enumerate(res):
            print(f"{index + 1}) {book_list[1]}")

    except ValueError as e:
        print(e)
    

if __name__ == "__main__":
    recommend_books(book_name="1984")