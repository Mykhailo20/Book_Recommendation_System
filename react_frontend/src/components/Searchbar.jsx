import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { GoSearch } from "react-icons/go";

const Searchbar = () => {

  const navigate = useNavigate();
  const [bookTitle, setBookTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    navigate(`/search/${bookTitle}`)
  }

  return (
    <form onSubmit={handleSubmit} autoComplete="off" className="p-2text-gray-400 focus-within:text-gray-600">
      <label htmlFor="search-field" className="sr-only">
        Search books
      </label>
      <div className="flex flex-row justify-start items-center">
        <GoSearch className="w-5 h-5 ml-4"/>
        <input
          name="search-field"
          autoComplete="off"
          id="search-field"
          placeholder="Search"
          type="search"
          value={bookTitle}
          onChange={ (e) => setBookTitle(e.target.value) }
          className="flex-1 bg-transparent border-none outline-none placeholder-gray-500 text-base text-white p-4"
        ></input>
      </div>
    </form>
  )
};

export default Searchbar;
