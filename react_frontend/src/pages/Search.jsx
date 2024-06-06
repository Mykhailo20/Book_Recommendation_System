import { useState } from 'react';

import { Searchbar, Error, BookCard, Loader } from '../components';
import { defaultAuthors } from '../assets/constants';
import { useGetAuthorsWithMostBooksQuery, useGetBooksByAuthorQuery } from '../redux/services/fastapiBackendCore';

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
  const [booksAuthor, setBooksAuthor] = useState(defaultAuthors[0].backendValue);
  
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
      <Searchbar />
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
