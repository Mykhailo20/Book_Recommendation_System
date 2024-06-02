import pickle

import pandas as pd

from book_recommendation_systems.utils.recommend_books import get_books_recommendations_1_book_rs
from config.data_config import ONE_BOOK_RS_RECOMMEND_BOOKS_NO


def recommend_books(books_df, pivot_table, similarity_scores, book_name, recommend_books_no=ONE_BOOK_RS_RECOMMEND_BOOKS_NO):
    
    res = (
        get_books_recommendations_1_book_rs(books_df=books_df, 
                                            book_name=book_name, 
                                            pivot_table=pivot_table, 
                                            similarity_scores=similarity_scores,
                                            recommend_books_no=recommend_books_no
        )
    )
    print(f"book_name: {book_name}")
    print(f"recommended_books: ")
    for index, book in enumerate(res):
        print(f"{index + 1}) {book.title}")
    return res

    
    
if __name__ == "__main__":
    books_df = pd.read_csv('../data/db_data/Books.csv')
    pivot_table = pickle.load(open('../artifacts/pivot_table.pkl', 'rb'))
    similarity_scores = pickle.load(open('../artifacts/similarity_scores.pkl', 'rb'))
    recommend_books(books_df=books_df, pivot_table=pivot_table, similarity_scores=similarity_scores, book_name="The Mists of Avalon")