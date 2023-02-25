import React from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";
 
 
class Canvas extends React.Component {
  constructor(props) {
    super(props);
    this.canvas = React.createRef();
  }

  state = {
    "guess": null,
  }

  BASE_URL = process.env.REACT_APP_BASE_URL || "localhost"


  preProcess(data){
    console.log("preProcess...")
    let cleaned =  data.map( line => line.paths.map(point => [Math.floor(Math.round(point.x * 100 ) / 100), Math.floor(Math.round(point.y * 100) / 100)] ))
    console.log("cleaned", cleaned)
    return cleaned
  }

  postData(processedData, url, category=null) {
    // console.log(processedData)
    const body = {data: processedData, category: category}
    fetch(url, {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body)
    })
    .then( res => res.json())
    .then(res => {
      console.log("response: ", res)
      this.setState({'guess': res})
    })
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
        <button className="btn-small waves-effect waves-light" 
          onClick={() => {
            this.canvas.current
              .exportPaths()
              .then(data => {
                let cleaned = this.preProcess(data)
                this.postData(cleaned, `http://${this.BASE_URL}/api/guess/`)
              })
              .catch(e => {
                console.log(e);
              });
          }}
        >
          Search
        </button>
        <div>
          <button className="btn-small waves-effect waves-light blue"           
          onClick={() => {
            this.canvas.current
              .exportPaths()
              .then(data => {
                let cleaned = this.preProcess(data)
                this.postData(cleaned, `http://${this.BASE_URL}/api/provide-sample/`, "X")
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
                let cleaned = this.preProcess(data)
                this.postData(cleaned, `http://${this.BASE_URL}/api/provide-sample/`, "O")
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

export default Canvas