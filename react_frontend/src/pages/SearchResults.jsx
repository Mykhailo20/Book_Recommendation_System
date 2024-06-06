import { useParams } from "react-router-dom";

import { Error, BookCard, Loader } from '../components';
import { useGetBooksByTitleQuery } from '../redux/services/fastapiBackendCore'

const SearchResults = () => {

    const bookTitle = useParams().bookTitle;

    console.log(`bookTitle = `, bookTitle);

    const {data: booksSearchData, isFetching: isFetchingBooksSearch, error: booksSearchError } =
    useGetBooksByTitleQuery({ bookTitle });
    
    console.log(`booksSearchData = `, booksSearchData);
    return (
        <div className='flex flex-col'>
          <div className='most-popular-books-container'>
              <div className='w-full flex justify-between items-center sm:flex-row flex-col mt-4 mb-10'>
                  <h2 className='font-bold text-2xl text-white text-left'>
                    Showing results for <span className="font-black">{ bookTitle  }</span>
                  </h2>
              </div>
              { isFetchingBooksSearch && <Loader title="Loading Books..."/> }
              { booksSearchError && <Error error="An error occurred while retrieving the most popular books."/>}
              {
                booksSearchData &&
                <div className='flex flex-wrap sm:justify-start justify-center gap-8'>
                    {booksSearchData?.map((book, index) => (
                        <BookCard
                            key={book.isbn}
                            book={book}
                            index={index}
                        />
                    ))}
                </div>
              }
          </div>
          
      </div>
    ) 
}

export default SearchResults;