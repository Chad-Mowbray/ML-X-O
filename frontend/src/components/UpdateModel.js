import {Component, createRef} from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";
import { preProcess } from "../utils/processor";
import { postData } from "../utils/api";
 
class Guess extends Component {
  
  
  canvas = createRef();
  state = {
    "guess": null,
  }


  handlePost = async (action, processedData=null, category=null) => {
    const data = postData(processedData, action, category)
    this.setState({"guess": data})
  }
 
  render() {
    return (
      <div className="center-within colored">
        <div className="top-margin">
          <ReactSketchCanvas
            ref={this.canvas}
            strokeWidth={10}
            strokeColor="black"
            width="99px"
            height="99px"/>
         </div>
        <button className="btn-small waves-effect waves-light" 
          onClick={() => {
            this.canvas.current
              .exportPaths()
              .then(data => {
                let cleaned = preProcess(data)
                postData("guess", cleaned)
              })
              .catch(e => {
                console.log(e);
              });
          }}
        >Guess</button>
      
          <button className="btn-small waves-effect waves-light red" 
          onClick= {() => {
            this.canvas.current.resetCanvas()
            this.setState({guess: null})
          }}>
            Clear
          </button>
          
          { this.state.guess && <p className="message">You probably drew an "{this.state.guess}"</p>}

        </div>
    );
  }
};

export default Guess