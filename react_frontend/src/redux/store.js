import { configureStore } from '@reduxjs/toolkit';
import { fastapiBackendCoreApi } from './services/fastapiBackendCore';

export const store = configureStore({
  reducer: {
    [fastapiBackendCoreApi.reducerPath]: fastapiBackendCoreApi.reducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(fastapiBackendCoreApi.middleware), 
});
