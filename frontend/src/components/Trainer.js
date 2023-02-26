import {useState, createRef} from "react";
import { Link } from 'react-router-dom'
import { cleanAndPost } from "../utils/api";
import MyCanvas  from "./MyCanvas";

 
const Trainer = () => {

  const canvas = createRef()

  const [train, setTrain] = useState(null)
  const [xCount, setXCount] = useState(0)
  const [oCount, setOCount] = useState(0)

  const handlePost = async (action, category=null) => {
    const data = await canvas.current.exportPaths()
    const res = await cleanAndPost(action, data, category)
    reset()
    setTrain(res["result"])
    setXCount(category === "X" ? xCount + 1 : xCount)
    setOCount(category === "O" ? oCount + 1 : oCount)
  }

  const reset = () => {
    canvas.current.resetCanvas()
    setTrain(null)
  }
 
    return (
      <>
        <div className="link"><Link to={"/"}>Home</Link></div>
        <div className="center-within colored">
          <div className="top-margin">
            <MyCanvas canvas={canvas}/>
          </div>
          <div>
            <button className="btn-small waves-effect waves-light blue"           
            onClick={() => handlePost("sample", "X")}>Train X</button>
            <button className="btn-small waves-effect waves-light blue"           
            onClick={() => handlePost("sample", "O")}>Train O</button>
            <button className="btn-small waves-effect waves-light red" 
            onClick={reset}>Clear</button>
            
            { train && 
            <p className="message">Thanks for submitting. {train} for training.</p>}
          </div>
            <div className="counts">
              <p>X count: {xCount}</p>
              <p>O count: {oCount}</p>
            </div>
        </div>
      </>
    );
};

export default Trainer