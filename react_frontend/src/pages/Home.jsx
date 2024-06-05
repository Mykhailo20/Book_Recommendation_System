import { useEffect, useState } from 'react';

import { Error, BookCard, Loader } from '../components';
import { useGetMostPopularBooksQuery } from '../redux/services/fastapiBackendCore';

const BASE_URL = 'http://localhost:8000/'

const Home = () => {

  const {data: mostPopularBooksData, isFetching: mostPopularBooksIsFetching, error: mostPopularBooksError } = useGetMostPopularBooksQuery();
  
  return (
      <div className='flex flex-col'>
          <div className='most-popular-books-container'>
              <div className='w-full flex justify-between items-center sm:flex-row flex-col mt-4 mb-10'>
                  <h2 className='font-bold text-2xl text-white text-left'>Most Popular Books</h2>
              </div>
              { mostPopularBooksIsFetching && <Loader title="Loading Books..."/> }
              { mostPopularBooksError && <Error error="An error occurred while retrieving the most popular books."/>}
              {
                mostPopularBooksData &&
                <div className='flex flex-wrap sm:justify-start justify-center gap-8'>
                    {mostPopularBooksData?.map((book, index) => (
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

export default Home;
