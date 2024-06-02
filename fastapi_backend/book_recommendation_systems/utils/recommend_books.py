from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
from sklearn.metrics.pairwise import cosine_similarity

from book_recommendation_systems.exceptions import DataIntegrityError

@dataclass
class Book:
    isbn: str
    title: str
    author: str
    publication_year: str
    publisher: str
    image_url: str


# from metrics import calc_book_score_df
def calc_book_score_df(ratings_df, 
                       book_recs_df,
                       ratings_df_cols={
                           'book_id': 'isbn',
                           'rating': 'rating',
                           'ratings_count': 'ratings_no',
                           'ratings_average': 'avg_rating'
                       }
):
    book_total_ratings_df = (
        ratings_df
        .groupby(ratings_df_cols['book_id'])
        [ratings_df_cols['rating']]
        .count()
        .reset_index()
        .rename(columns = {ratings_df_cols['rating']: 'total_ratings_no'})
    )

    book_recs_df = book_recs_df.merge(book_total_ratings_df, how='inner', on=ratings_df_cols['book_id'])

    # Create the 'book_score' variable to recommend books
    book_recs_df['adjusted_ratings_no'] = book_recs_df[ratings_df_cols['ratings_count']] * (book_recs_df[ratings_df_cols['ratings_count']] / book_recs_df['total_ratings_no'])
    book_recs_df['book_score'] = book_recs_df[ratings_df_cols['ratings_average']] * book_recs_df['adjusted_ratings_no']
    
    return book_recs_df


MIN_USERS_OVERLAP_COEFF = 0.5   # The minimum percentage of co-read books between current_user and overlapped_user to be used to create a recommendation
MIN_BOOKS_NO_TO_USE_OVERLAP_COEFF = 2   # The minimum number of books read and rated by current_user before the MIN_USERS_OVERLAP_COEFF factor will be used to filter overlapped_users
SIMILAR_USERS_NO = 15   # The number of similar users whose book preferences will be used to recommend books to the current_user
MIN_BOOK_RATINGS_NO_CFB = 3   # The minimum number of ratings for a single book to be used to build a Collaborative Filtering Based Recommender System
BOOKS_NO_TO_RECOMMEND = 10   # The number of books that will be recommended to the user based on his/her book list


def get_books_recommendations_1_book_rs(books_df, book_name, pivot_table, similarity_scores, recommend_books_no=5,
                   books_df_cols={
                      'book_isbn': 'isbn',
                      'book_title': 'title',
                      'book_author': 'author',
                      'book_publication_year': 'publication_year',
                      'book_publisher': 'publisher',
                      'book_image': 'image_url'
                   }):
    """
    Recommends books similar to the given book based on similarity scores.

    Args:
        books_df (pd.DataFrame): The DataFrame containing the books data.
        book_name (str): The name of the book for which recommendations are to be made.
        pivot_table (pd.DataFrame or scipy.sparse.csr_matrix): The pivot table containing book-user interactions.
        similarity_scores (np.ndarray): The matrix of cosine similarity scores.
        recommend_books_no (int, optional): The number of similar books to recommend. Default is 5.
        books_df_cols (dict, optional): A dictionary mapping the standard column names to the DataFrame column names.
            - 'book_isbn' (str): Column name for the book's ISBN.
            - 'book_title' (str): Column name for the book's title.
            - 'book_author' (str): Column name for the book's author.
            - 'book_image' (str): Column name for the book's image URL.
        
    Raises:
        ValueError: If the specified book is not found in the pivot table.
    
    Returns:
        list: A list of books.
    """
    
    if book_name not in pivot_table.index:
        raise ValueError(f"Book '{book_name}' not found in the dataset.")
        
    index = np.where(pivot_table.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:(recommend_books_no + 1)]
    
    data = []
    for i in similar_items:
        
        temp_df = books_df[books_df['title'] == pivot_table.index[i[0]]]
        temp_df = temp_df.drop_duplicates(books_df_cols['book_title'])
        if len(temp_df) > 1:
            raise DataIntegrityError(f"Data integrity error (One book Recommender System): Multiple entries found for title '{pivot_table.index[i[0]]}' after removing duplicates.")
        book = Book(
            isbn=temp_df[books_df_cols['book_isbn']].values[0],
            title=temp_df[books_df_cols['book_title']].values[0],
            author=temp_df[books_df_cols['book_author']].values[0],
            publication_year=int(temp_df[books_df_cols['book_publication_year']].values[0]),
            publisher=temp_df[books_df_cols['book_publisher']].values[0],
            image_url=temp_df[books_df_cols['book_image']].values[0]
        )        
        data.append(book)
    
    return data


def get_similar_readers(ratings_df, books_user_like_isbn_set, min_books_no_overlap_coeff, min_users_overlap_coeff):
    filtered_ratings_df = ratings_df[ratings_df['isbn'].isin(books_user_like_isbn_set)]

    overlap_users_series = (
        filtered_ratings_df
        .groupby('user_id')
        .count()
        .reset_index()
        .rename(columns={'rating': 'ratings_no'})
    )

    """ 
        Filter users, leaving only those who have read all the books of current_user 
            (if len(books_user_like) <= MIN_BOOKS_NO_TO_USE_OVERLAP_COEFF) 
        or MIN_USERS_OVERLAP_COEFF a part of the books read by current_user 
            (if len(books_user_like) > MIN_BOOKS_NO_TO_USE_OVERLAP_COEFF)
    """

    filtered_overlap_user_ids_set = None
    if len(books_user_like_isbn_set) <= min_books_no_overlap_coeff: 
        books_thresh = len(books_user_like_isbn_set)
        filtered_overlap_user_ids_set = set(overlap_users_series[overlap_users_series['ratings_no'] >= books_thresh]['user_id'].values)
    else:
        books_thresh = int(len(books_user_like_isbn_set) * min_users_overlap_coeff)
        filtered_overlap_user_ids_set = set(overlap_users_series[overlap_users_series['ratings_no'] > books_thresh]['user_id'].values)
    
    return filtered_overlap_user_ids_set


def get_similar_book_ratings(ratings_df, books_user_like_df, filtered_overlap_user_ids_set):
    interactions_arr = ratings_df[(
        ratings_df['user_id']
        .apply(lambda user_id: user_id in filtered_overlap_user_ids_set)
    )].values

    interactions_df = pd.DataFrame(data=interactions_arr, columns=['user_id', 'isbn', 'rating'])
    interactions_df = pd.concat([books_user_like_df[['user_id', 'isbn', 'rating']], interactions_df])
    interactions_df['user_id'] = pd.to_numeric(interactions_df['user_id'])
    interactions_df['rating'] = pd.to_numeric(interactions_df['rating'])

    interactions_df['user_index'] = interactions_df['user_id'].astype('category').cat.codes
    interactions_df['book_index'] = interactions_df['isbn'].astype('category').cat.codes

    ratings_matrix_coo = coo_matrix((interactions_df['rating'], (interactions_df['user_index'], interactions_df['book_index'])))
    ratings_matrix = ratings_matrix_coo.tocsr()

    return interactions_df, ratings_matrix


def get_cosine_similar_readers(current_user_index, ratings_matrix, interactions_df, similar_users_no):
    similarity = cosine_similarity(ratings_matrix[current_user_index, :], ratings_matrix).flatten()
    similar_user_indices = np.argpartition(similarity, -(similar_users_no + 1))[-(similar_users_no + 1):]
    similar_user_indices = np.delete(similar_user_indices, np.where(similar_user_indices == 0))
    similar_users = interactions_df[interactions_df['user_index'].isin(similar_user_indices)].copy()
    return similar_users


def get_title_filtered_books(book_recs_df, books_user_like_df):
    book_recs_df['mod_title'] = book_recs_df['title'].str.replace("[^a-zA-Z0-9 ]", "", regex=True).str.lower()
    book_recs_df['mod_title'] = book_recs_df['mod_title'].str.replace("\s+", " ", regex=True)

    books_user_like_df['mod_title'] = books_user_like_df['title'].str.replace("[^a-zA-Z0-9 ]", "", regex=True).str.lower()
    books_user_like_df['mod_title'] = books_user_like_df['mod_title'].str.replace("\s+", " ", regex=True)

    book_recs_df = book_recs_df[~book_recs_df['mod_title'].isin(books_user_like_df['mod_title'])]
    return book_recs_df

def get_books_recommendations_books_list_rs(ratings_df, books_df, books_user_like_df):
    books_user_like_isbn_set = set(books_user_like_df['isbn'])   # Because theoretically, a user could give several ratings to a book with the same isbn

    # Find users with similar book preferences as the current user
    filtered_overlap_user_ids_set = get_similar_readers(
        ratings_df, 
        books_user_like_isbn_set, 
        min_books_no_overlap_coeff=MIN_BOOKS_NO_TO_USE_OVERLAP_COEFF,
        min_users_overlap_coeff=MIN_USERS_OVERLAP_COEFF
    )
    
    # Find similar user book ratings
    interactions_df, ratings_matrix = get_similar_book_ratings(ratings_df, books_user_like_df, filtered_overlap_user_ids_set)

    # Find users similar to current_user
    current_user_index = interactions_df[interactions_df['user_id'] == -1]['user_index'].unique()[0]    # Get user_index for the current_user
    similar_users = get_cosine_similar_readers(current_user_index, ratings_matrix, interactions_df, similar_users_no=SIMILAR_USERS_NO)

    # Create book recommendations using the 'book_score' variable
    book_recs_df = (
        similar_users
        .groupby('isbn')
        ['rating']
        .agg(['count', 'mean'])
        .rename(columns = {
            'count': 'ratings_no',
            'mean': 'avg_rating'
        })
        .sort_values(by='ratings_no', ascending=False)
    )

    # merge book_recs_df and books_df to get all the information about recommended books
    book_recs_df = book_recs_df.merge(books_df, how='inner', on='isbn')
    book_recs_df = book_recs_df[book_recs_df['ratings_no'] >= MIN_BOOK_RATINGS_NO_CFB]
    book_recs_df = calc_book_score_df(ratings_df, book_recs_df)

    # Filter the results and recommend books
    book_recs_df = book_recs_df[~book_recs_df['isbn'].isin(books_user_like_df['isbn'])]
    book_recs_df = get_title_filtered_books(book_recs_df, books_user_like_df)
    top_books_recs_df = book_recs_df.drop_duplicates('title').sort_values(by='book_score', ascending=False)
    return top_books_recs_df.head(BOOKS_NO_TO_RECOMMEND)
    