import { Link } from 'react-router-dom';

const BookCard = ({ book, index }) => {
  const activeBook = 'Test';
    return(
    <div className='flex flex-col w-[225px] p-4 bg-white/5 
                    bg-opacity-80 dackdrop-blur-sm animate-slideup 
                    rounded-lg cursor-pointer'>
      <div className='relative w-full group'>
        <div className={`absolute inset-0 justify-center items-center bg-black
                         bg-opacity-20 group-hover:flex hidden`}>
        </div>
        <div className='w-100 flex justify-center'>
          { book.image_url ? (
              <img alt='book_img' src={ book.image_url } className='min-h-[10rem]' />
            ) : (
              <div
                style={{
                  width: '220px',
                  height: '131.741px',
                  backgroundColor: 'gray',
                }}
              />
            )}
          
        </div>
      </div>
      <div className='mt-4 flex flex-col'>
        <p className='font-semibold text-400 text-center text-white'>
          <Link to={`/books/${book?.isbn}`}>
            {book.title}
          </Link>
        </p>
        <p className="text-sm truncate text-gray-300  text-center mt-1">
            {book.author}
        </p>
      </div>
    </div>
  )
};

export default BookCard;
