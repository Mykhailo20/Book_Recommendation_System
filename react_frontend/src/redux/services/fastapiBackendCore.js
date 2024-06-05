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
    }),
});

export const {
    useGetMostPopularBooksQuery,
} = fastapiBackendCoreApi;