import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const fastapiBackendCoreApi = createApi({
    reducerPath: 'fastapiBackendCoreApi',
    baseQuery: fetchBaseQuery({
        baseUrl: 'http://localhost:8000',
        prepareHeaders: (headers) => {
            return headers;
        }
    }),
    endpoints: (builder) => ({
        getMostPopularBooks: builder.query({ query: () => '/book/most_popular' }),
        getBookDetails: builder.query({ query: ({ bookIsbn }) => `/book/${bookIsbn}` }),
        getSimilarBooks: builder.query({ query: ({ bookIsbn }) => `/book/similar/${bookIsbn}` }),
        getAuthorsWithMostBooks: builder.query({ query: (booksNo=50) => `/book/authors_most_books?books_no=${booksNo}` })
    }),
});

export const {
    useGetMostPopularBooksQuery,
    useGetBookDetailsQuery,
    useGetSimilarBooksQuery,
    useGetAuthorsWithMostBooksQuery
} = fastapiBackendCoreApi;