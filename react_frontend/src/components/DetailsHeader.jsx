const DetailsHeader = ({ bookData }) => (
  <div className="relative w-full flex flex-col top-5">
    <div className="w-full bg-gradient-to-l from-transparent to-black
      sm:h-56 h-48
    ">
      <div className="absolute inset-0 flex items-start">
        <img src={ bookData?.image_url }
          className="sm:w-36 w-28 rounded-sm object-cover shadow-xl shadow-black" 
          alt="book-img"
        />
        <div className="ml-5">
          <div className="book_title mb-10">
            <p className="font-bold sm:text-3xl text-xl text-white">{ bookData?.title }</p>
          </div>
          <div className="book_details">
            <p className="text-base text-gray-400 mt-2"><strong>Author:</strong> { bookData?.author }</p>
            <p className="text-base text-gray-400 mt-2"><strong>Publisher:</strong> { bookData?.publisher }</p>
            {
              bookData?.publication_year !== 0? (
                <p className="text-base text-gray-400 mt-2">
                <strong>Publication year:</strong> { bookData?.publication_year }</p>
              ):(
                <></>
              )
            }
          </div>
        </div>
      </div>
    </div>
  </div>
);

export default DetailsHeader;
