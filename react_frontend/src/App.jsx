import { Route, Routes } from 'react-router-dom';

import { Searchbar, Sidebar } from './components';
import { Home, Search, BookDetails, SearchResults } from './pages';

const App = () => {

  return (
    <div className="relative flex">
      <Sidebar />
      <div className="flex-1 flex flex-col bg-gradient-to-br from-black to-[#121286]">
        <div className='header mb-5 bg-white'></div>
        <Searchbar />

        <div className="px-6 h-[calc(100vh)] overflow-y-scroll hide-scrollbar flex xl:flex-row flex-col-reverse">
          <div className="flex-1 h-fit pb-32">
            <Routes>
              <Route path="/" element={< Home />} />
              <Route path="/books/:bookIsbn" element={< BookDetails />} />
              <Route path="/search/:bookTitle" element={< SearchResults />} />
              <Route path="/search" element={< Search />} />
            </Routes>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
