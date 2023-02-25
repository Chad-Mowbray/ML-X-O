import {Component, createRef} from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";
import { preProcess } from "../utils/processor";
import { postData } from "../utils/api";
 
 
class Trainer extends Component {

  
  canvas = createRef();

  state = {
    "guess": null,
  }


  handlePost = async (processedData, action, category=null) => {
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
            height="99px"
          />
         </div>
        <div>
          <button className="btn-small waves-effect waves-light blue"           
          onClick={() => {
            this.canvas.current
              .exportPaths()
              .then(data => {
                let cleaned = preProcess(data)
                postData("sample", cleaned, "X")
              })
              .catch(e => {
                console.log(e);
              });
          }}>Train X</button>
          <button className="btn-small waves-effect waves-light blue"           
          onClick={() => {
            this.canvas.current
              .exportPaths()
              .then(data => {
                let cleaned = preProcess(data)
                postData("sample", cleaned, "O")
              })
              .catch(e => {
                console.log(e);
              });
          }}>Train O</button>
          <button className="btn-small waves-effect waves-light red" 
          onClick= {() => {
            this.canvas.current.resetCanvas()
            this.setState({guess: null})
          }}>
            Clear
          </button>
          
          { this.state.guess && <p className="message">You probably drew an "{this.state.guess}"</p>}

        </div>
        
      </div>
    );
  }
};

export default Trainer