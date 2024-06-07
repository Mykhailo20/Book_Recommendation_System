import { useNavigate } from 'react-router-dom';
import { FaHouseUser, FaBookOpen } from "react-icons/fa";

import { libraryImg } from '../assets';
import { Error, BookCard, Loader } from '../components';
import { useGetMostPopularBooksQuery } from '../redux/services/fastapiBackendCore';

const Home = () => {

  const {data: mostPopularBooksData, isFetching: isFetchingMostPopularBooks, error: mostPopularBooksError } = useGetMostPopularBooksQuery();
  const navigate = useNavigate();

  return (
    <div className='flex flex-col'>
        {/* Proverb about books */}
        <div className='flex justify-center'>
            <div className="flex items-center justify-center p-6 rounded-lg shadow-md mb-12 w-1/2">
                <FaBookOpen className="text-yellow-600 w-8 h-8 mr-4" />
                <p className="font-bold text-2xl text-white text-left">
                    A book holds a house of gold
                </p>
                <FaHouseUser className="text-yellow-600 w-8 h-8 ml-4" />
            </div>
        </div>
        
        {/* Find Next Book */}
        <div className='find-next-book-container flex flex-row justify-around mb-10'>
            <div className='flex flex-col justify-center align-middle'>
                <h2 className='font-bold text-2xl text-white text-left mb-2 sm:mb-6 md:mb-3'>Find your next book to read</h2>
                <button 
                    className='bg-transparent text-gray-300 border border-white p-2 rounded-lg self-start hover:text-red-500 hover:border-red-500'
                    onClick={() => navigate(`/search`) }
                >
                    Explore
                </button>
            </div>
            <img
                src={libraryImg} 
                className='rounded-md
                           w-56 sm:w-64 md:w-80 lg:w-96 xl:w-1/3 2xl:w-2/5
                           mr-2 sm:mr-3 md:mr-4 lg:mr-5 xl:mr-6 2xl:r-7'
            />
        </div>

        {/* Most Popular Books */}
        <div className='most-popular-books-container'>
            <div className='w-full flex justify-between items-center sm:flex-row flex-col mt-4 mb-10'>
                <h2 className='font-bold text-2xl text-white text-left'>Most Popular Books</h2>
            </div>
            { isFetchingMostPopularBooks && <Loader title="Loading Books..."/> }
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
