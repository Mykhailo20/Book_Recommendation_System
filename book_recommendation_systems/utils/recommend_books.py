import numpy as np


def get_books_recommendations_1_book_rs(books_df, book_name, pivot_table, similarity_scores, recommend_books_no=5,
                   books_df_cols={
                      'book_isbn': 'isbn',
                      'book_title': 'title',
                      'book_author': 'author',
                      'book_image': 'image-url-l'
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
        list: A list of lists, each containing the details of a recommended book (ISBN, title, author, image URL).
    """
    
    if book_name not in pivot_table.index:
        raise ValueError(f"Book '{book_name}' not found in the dataset.")
        
    index = np.where(pivot_table.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:(recommend_books_no + 1)]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = books_df[books_df['title'] == pivot_table.index[i[0]]]
        temp_df = temp_df.drop_duplicates(books_df_cols['book_title'])
        
        item.extend(list(temp_df[books_df_cols['book_isbn']].values))
        item.extend(list(temp_df[books_df_cols['book_title']].values))
        item.extend(list(temp_df[books_df_cols['book_author']].values))
        item.extend(list(temp_df[books_df_cols['book_image']].values))
        
        data.append(item)
    
    return data
