import './App.css';
import Canvas from './components/Canvas'
import Header from './components/Header'
import Guess from './components/UpdateModel'
import Trainer from './components/Trainer'
import UpdateModel from './components/Guess';
import {HashRouter, Routes, Route} from 'react-router-dom'


function App() {
  return (
    <div className="">
      <HashRouter>
      <Header />
      <Routes>
        <Route path="/training-data" element={<Trainer />}/>
        <Route path="/guess" element={<Guess />}/>
        <Route path="/update-model" element={<UpdateModel />}/>
        <Route exact path="/"  element={ <Header />}/>
      </Routes>
      
      </HashRouter>
      {/* <Canvas /> */}
    </div>
  );
}

export default App;
