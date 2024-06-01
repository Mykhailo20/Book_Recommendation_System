def calc_weighted_rating(row, avg_rating, num_of_ratings, min_thres, default_rating):
    """
    Calculates the weighted rating for a book based on its average rating, number of ratings, and a minimum threshold.

    Args:
        row (pd.Series): A row from the DataFrame containing the book's data.
        avg_rating (str): The column name for the average rating of the book.
        num_of_ratings (str): The column name for the number of ratings the book has received.
        min_thres (int): The minimum threshold for the number of ratings to be considered for the weighted rating.
        default_rating (float): The neutral rating of the book.

    Returns:
        float: The calculated weighted rating for the book.
    """
    
    weighted_rating = ((row[avg_rating] * row[num_of_ratings]) + 
      (min_thres * default_rating))/(row[num_of_ratings] + min_thres)
    return weighted_rating


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