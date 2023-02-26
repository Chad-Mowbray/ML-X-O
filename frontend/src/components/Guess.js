import {createRef, useState} from "react";
import { Link } from 'react-router-dom'
import { cleanAndPost } from "../utils/api";
import MyCanvas from "./MyCanvas";

const Guess = () => {
  
  const canvas = createRef()

  const [guess, setGuess] = useState(null)
  const [numSamples, setNumSamples] = useState(0)


  const handlePost = async (action, category=null) => {
    const data = await canvas.current.exportPaths()
    const res = await cleanAndPost(action, data, category)
    reset()
    setGuess(res["best_guess"])
    setNumSamples(res["num_samples"])
  }

  const reset = () => {
    canvas.current.resetCanvas()
    setGuess(null)
  }

  const getMessage = () => {
    if (guess === "NONE") {
      return <Link to="/training-data">The model has not been trained yet.</Link>
    } else {
      return`You probably drew an ${guess}.  This model was trained on ${numSamples} examples`
    }
  }

    return (
      <>
        <div className="link"><Link to={"/"}>Home</Link></div>
        <div className="center-within colored">
          <div className="top-margin">
            <MyCanvas canvas={canvas}/>
          </div>
          <button className="btn-small waves-effect waves-light" 
            onClick={() => handlePost("guess")}>Guess</button>
          <button className="btn-small waves-effect waves-light red" 
          onClick= {reset}>Clear</button>
            
          { guess && 
          <p className="message">{getMessage()}</p>}
        </div>
      </>
    );

};

export default Guess