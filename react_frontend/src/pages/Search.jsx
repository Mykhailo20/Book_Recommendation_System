import { Searchbar } from '../components';
import { defaultAuthors } from '../assets/constants';
import { useGetAuthorsWithMostBooksQuery } from '../redux/services/fastapiBackendCore';

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
    displayValue: processBackendAuthor(backendValue),
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

const Search = () => {

  const bookAuthor = defaultAuthors[0].frontendValue;
  const {data: authorsData, isFetching: isFetchingAuthorsData, error: authorsDataError } = 
  useGetAuthorsWithMostBooksQuery();


  let authorsArray = []

  authorsArray = authorsData? mergeAuthors(defaultAuthors, authorsData): defaultAuthors;

  return (
    <div>
      <Searchbar />
      <div className='w-full flex justify-between items-center
                      sm:flex-row flex-col mt-4 mb-10
      '>
        <h2 className="font-bold text-3xl text-white text-left">Search for books by author</h2>
        <select
          onChange={ () => {} }
          value={ bookAuthor }
          className="bg-black text-gray-300 p-3 text-sm rounded-lg outline-none sm:mt-0 mt-5"
        >
          { authorsArray.map(
            (author) => 
              <option key={author.backendValue} value={author.backendValue}>
                {author.displayValue}
              </option>
          )}
        </select>
      </div>
      
    </div>
  )
  
};

export default Search;
