import { useState } from 'react';

import { defaultTitles } from '../assets/constants';
import { useGetSimilarBooksAllTitlesQuery } from '../redux/services/fastapiBackendCore';

const SimilarBooksOneBookRS = () => {
    const [bookTitle, setBookTitle] = useState(defaultTitles[0]);
    const { data: allTitlesRSData, isFetching: isFetchingAllTitlesRSData, error: allTitlesRSDataError } = useGetSimilarBooksAllTitlesQuery();

    let titlesArray = allTitlesRSData ? allTitlesRSData : defaultTitles;

    return (
        <>
            <div className='w-full flex justify-between items-left
                      flex-col mt-4 mb-10
            '>
                <h2 className='font-bold text-3xl text-white text-left mb-10'>Find similar books</h2>
                <select
                    onChange={ (e) => {setBookTitle(e.target.value)} }
                    value={ bookTitle }
                    className="bg-black text-gray-300 p-4 text-sm rounded-lg outline-none sm:mt-0 mt-5"
                    >
                    { titlesArray.map(
                        (title) => 
                        <option key={title} value={title}>
                            {title}
                        </option>
                    )}
                    </select>
            </div>
        </>
    )
}

export default SimilarBooksOneBookRS;