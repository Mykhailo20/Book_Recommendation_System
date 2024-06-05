import { useEffect, useState } from 'react';

import { Error, BookCard } from '../components';
import { useGetMostPopularBooksQuery } from '../redux/services/fastapiBackendCore';

const BASE_URL = 'http://localhost:8000/'

const Home = () => {

  const {data, isFetching, error } = useGetMostPopularBooksQuery();
  console.log(data);
    /*const [mostPopularBooks, setMostPopularBooks] = useState([]);
    useEffect(() => {
        
        fetch(BASE_URL + 'book/most_popular')
          .then(response => {
            const json = response.json()
            console.log(`fetch books: `, json)
            if(response.ok) {
              return json
            }
            throw response
          })
          .then(data => {
            setMostPopularBooks(data)
          })
          .catch(error => {
            console.log(error)
          })
      }, []);*/

    return (
        <div className='flex flex-col'>
            <div className='most-popular-books-container'>
                <div className='w-full flex justify-between items-center sm:flex-row flex-col mt-4 mb-10'>
                    <h2 className='font-bold text-2xl text-white text-left'>Most Popular Books</h2>
                </div>
                <div className='flex flex-wrap sm:justify-start justify-center gap-8'>
                    {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((book, index) => (
                        <BookCard
                            key={book.isbn}
                            book={book}
                            index={index}
                        />
                    ))}
                </div>
            </div>
            
        </div>
        
    )
    
}

export default Home;
