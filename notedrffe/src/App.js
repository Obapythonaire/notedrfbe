// import React from "react";
import {
  // BrowserRouter as Router,
  // Changing Browserrouter to Hashrouter to solve CSRF issue and page reload issue.
  HashRouter as Router,
  Route,
  Routes,
} from "react-router-dom";

import './App.css';
import Header from './components/Header';
// import Body from './components/Body';
import Footer from './components/Footer';
import NotesListPage from './pages/NotesListPage';
import NotePage from './pages/NotePage';

function App() {
  return (
    <Router>
      <div className="container dark">
        <div className="app">
        {/* <b>My Project</b> */}
        <Header />
        <Routes>
          {/* <Route> */}
            {/* <Body /> */}
            {/* <NotesListPage /> */}
            {/* The Below method is defunct since the release of version 6 */}
            {/* <Route path="/" exact component={NotesListPage} /> */}

            {/* Below is the new and working method in version 6 */}
            <Route path="/" element={<NotesListPage />} />
            <Route path="/note/:id" element={<NotePage />} />
          {/* </Route> */}
        </Routes>
        <Footer />
        </div>
      </div>
    </Router>
  );
}

export default App;




// Starter Code
// 
// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
