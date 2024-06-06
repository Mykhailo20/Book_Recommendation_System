import { useParams } from "react-router-dom";
import { DetailsHeader, Error, Loader, SimilarBooks } from "../components";

import { useGetBookDetailsQuery } from "../redux/services/fastapiBackendCore";

const BookDetails = () => {

    const { bookIsbn } = useParams();
    const {data: bookData, isFetching: isFetchingBookData, error: bookDataError } = useGetBookDetailsQuery({ bookIsbn })
    
    return (
        <div className="flex flex-col">
            { isFetchingBookData && <Loader title="Loading Book Data..."/> }
            { bookDataError && <Error error="An error occurred while retrieving the book data."/> }
            { bookData && <DetailsHeader bookData={bookData} /> }

            { /* Similar Books Container */ }
            <SimilarBooks bookIsbn={ bookIsbn } />
        </div>
    )
}

export default BookDetails;
