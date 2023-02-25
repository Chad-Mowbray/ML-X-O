import {Component, createRef} from "react";
import { cleanAndPost } from "../utils/api";
import { getCanvas } from "./Canvas";
 
class Guess extends Component {
  
  canvas = createRef()

  state = {
    "guess": null,
  }


  handlePost = async (action, category=null) => {
    const data = await this.canvas.current.exportPaths()
    const cleanedData = cleanAndPost(action, data, category)
    this.setState({"guess": cleanedData})
  }

  reset = () => {
    this.canvas.current.resetCanvas()
    this.setState({guess: null})
  }

 
  render() {
    return (
      <div className="center-within colored">
        <div className="top-margin">
          {getCanvas()}
         </div>
        <button className="btn-small waves-effect waves-light" 
          onClick={() => this.handlePost("guess")}>Guess</button>
    
          <button className="btn-small waves-effect waves-light red" 
          onClick= {() => this.reset()}>Clear</button>
          
          { this.state.guess && 
          <p className="message">You probably drew an "{this.state.guess}"</p>}

        </div>
    );
  }
};

export default Guess