import './App.css';
import Home from './components/Home'
import Guess from './components/UpdateModel'
import Trainer from './components/Trainer'
import UpdateModel from './components/Guess';
import {HashRouter, Routes, Route} from 'react-router-dom'


function App() {
  return (
    <div className="">
      <HashRouter>
        <Routes>
          <Route path="/training-data" element={<Trainer />}/>
          <Route path="/guess" element={<Guess />}/>
          <Route path="/update-model" element={<UpdateModel />}/>
          <Route exact path="/"  element={ <Home />}/>
        </Routes>
      
      </HashRouter>
    </div>
  );
}

export default App;
