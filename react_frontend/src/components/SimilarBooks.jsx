import { BookCard, Error, Loader } from "../components";
import { useGetSimilarBooksByIsbnQuery, useGetSimilarBooksByTitleQuery } from "../redux/services/fastapiBackendCore";

const SimilarBooks = ({ bookIsbn, bookTitle, h2Title }) => {
  let hookToUse = null;
  let hookToUseParam = null;
  if(bookIsbn){
    hookToUse = useGetSimilarBooksByIsbnQuery;
    hookToUseParam = bookIsbn;
  } else if(bookTitle) {
    hookToUse = useGetSimilarBooksByTitleQuery;
    hookToUseParam = bookTitle;
  }
  const {data: similarBooksData, isFetching: isFetchingSimilarBooksData, error: similarBooksDataError } = hookToUse(hookToUseParam)
  return (
    <div className='flex flex-col mt-5'>
      <div className='most-popular-books-container'>
          <div className='w-full flex justify-between items-center sm:flex-row flex-col mt-4 mb-4'>
            {similarBooksData && 
              <h2 className='font-bold text-2xl text-white text-left'>{ h2Title? h2Title: 'Similar Books' }</h2>
            }
            
          </div>
          { isFetchingSimilarBooksData && <Loader title="Loading Similar Books Data..."/> }
          { similarBooksDataError && similarBooksDataError.status !== 404 ?
                    (
                      <Error error="An error occurred while retrieving the similar books data."/> 
                    ):similarBooksDataError ? (
                         <></>
                    ):(
                        <></>
                    )
              }
          {
            similarBooksData &&
            <div className='flex flex-wrap sm:justify-start justify-center gap-8'>
                {similarBooksData?.map((book, index) => (
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
};
  
  export default SimilarBooks;