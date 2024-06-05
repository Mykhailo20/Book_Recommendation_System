import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { DetailsHeader, Error, Loader, SimilarBooks } from "../components";

import { useGetBookDetailsQuery } from "../redux/services/fastapiBackendCore";

const BookDetails = () => {

    const { bookIsbn } = useParams();
    const {data: bookData, isFetching: isFetchingBookData, error: fetchBookDataError } = useGetBookDetailsQuery({ bookIsbn })
    console.log(`bookData = `, bookData);

    return (
        <div className="flex flex-col">
            <DetailsHeader bookData={bookData} />
            
        </div>
    )
}

export default BookDetails;
