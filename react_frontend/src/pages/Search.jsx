import { useState } from 'react';

import { Error, BookCard, Loader, SimilarBooks } from '../components';
import { defaultTitles, defaultAuthors } from '../assets/constants';
import { useGetAuthorsWithMostBooksQuery, useGetBooksByAuthorQuery, useGetSimilarBooksAllTitlesQuery } 
from '../redux/services/fastapiBackendCore';

const processBackendAuthor = (backendValue) => {
  const words = backendValue.split(' ');
  if (words.length <= 2) {
    return backendValue;
  } else {
    return `${words[0]} ${words[words.length - 1]}`;
  }
};

const mergeAuthors = (defaultAuthors, authorsData) => {
  const processedAuthorsData = authorsData.map(backendValue => ({
    frontendValue: processBackendAuthor(backendValue),
    backendValue: backendValue
  }));

  const mergedAuthors = [...defaultAuthors];

  processedAuthorsData.forEach(author => {
    if (!mergedAuthors.some(existingAuthor => existingAuthor.backendValue === author.backendValue)) {
      mergedAuthors.push(author);
    }
  });

  return mergedAuthors;
};

const getUniqueBooksByTitle = (books) => {
  const titles = new Set();
  return books.filter((book) => {
    if (titles.has(book.title) || book.title.includes('Edition') || book.title.includes('Audio')) {
      return false;
    } else {
      titles.add(book.title);
      return true;
    }
  });
};

const Search = () => {
  const [bookTitle, setBookTitle] = useState('');
  const [booksAuthor, setBooksAuthor] = useState(defaultAuthors[0].backendValue);
  
  // Get similar books
  const { data: allTitlesRSData, isFetching: isFetchingAllTitlesRSData, error: allTitlesRSDataError } = useGetSimilarBooksAllTitlesQuery();
  let titlesArray = allTitlesRSData ? allTitlesRSData : defaultTitles;

  // Search books by author
  const {data: authorsData, isFetching: isFetchingAuthorsData, error: authorsDataError } = 
  useGetAuthorsWithMostBooksQuery();

  const {data: authorBooksData, isFetching: isFetchingAuthorBooksData, error: authorBooksDataError } = 
  useGetBooksByAuthorQuery({ booksAuthor });

  let authorsArray = []
  authorsArray = authorsData? mergeAuthors(defaultAuthors, authorsData): defaultAuthors;
  const frontendAuthor = authorsArray.find(({ backendValue }) => backendValue === booksAuthor)?.frontendValue;
  const uniqueBooks = authorBooksData ? getUniqueBooksByTitle(authorBooksData) : [];

  return (
    <div>
      { /* Get similar books by title */ }
      <div className='w-full flex justify-between items-left flex-col mt-4 mb-12'>
          <h2 className='font-bold text-3xl text-white text-left mb-10'>Find similar books</h2>
          <div className='flex items-left flex-col'>
              <select                  
                  className="bg-black text-gray-300 p-4 text-sm rounded-lg outline-none sm:mt-0 mt-5 mb-2"
                  id="bookTitleSelect"
                  >
                  { titlesArray.map(
                      (title) => 
                      <option key={title} value={title}>
                          {title}
                      </option>
                  )}
              </select>
              <button 
                  className='bg-transparent text-gray-300 border border-white p-3 rounded-lg self-start hover:bg-black hover:border-black'
                  onClick={() => {
                    const selectedTitle = document.getElementById("bookTitleSelect").value;
                    setBookTitle(selectedTitle);
                  }}
              >
                  Show Recommendations
              </button>
          </div>
          {
            bookTitle &&
            <SimilarBooks bookTitle={ bookTitle } h2Title={`Books similar to the book '${bookTitle}'`} />
          }
      </div>

      { /* Search books by author */ }
      <div className='w-full flex justify-between items-center
                      sm:flex-row flex-col mt-4 mb-10
      '>
        <h2 className="font-bold text-3xl text-white text-left">Search books by author</h2>
        <select
          onChange={ (e) => {setBooksAuthor(e.target.value)} }
          value={ booksAuthor }
          className="bg-black text-gray-300 p-3 text-sm rounded-lg outline-none sm:mt-0 mt-5"
        >
          { authorsArray.map(
            (author) => 
              <option key={author.backendValue} value={author.backendValue}>
                {author.frontendValue}
              </option>
          )}
        </select>
      </div>
      <div className='mt-5'>
        { isFetchingAuthorBooksData && <Loader title={ `Loading Books by ${frontendAuthor}...` }/> }
        { authorBooksDataError && <Error error={ `An error occurred while receiving books by ${frontendAuthor}` }/>}
        {
          uniqueBooks &&
          <>
            <h3 className="font-bold text-2xl text-white text-left mb-5">
              {`Books by ${frontendAuthor} (${uniqueBooks.length} found)`}
            </h3>
            <div className='flex flex-wrap sm:justify-start justify-center gap-8'>
                {uniqueBooks.map((book, index) => (
                    <BookCard
                        key={book.isbn}
                        book={book}
                        index={index}
                    />
                ))}
            </div>
          </>
        }
      </div>
    </div>
  )
  
};

export default Search;
