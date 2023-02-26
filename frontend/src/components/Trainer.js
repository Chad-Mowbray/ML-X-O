import {Component, createRef} from "react";
import { Link } from 'react-router-dom'
import { cleanAndPost } from "../utils/api";
import MyCanvas  from "./MyCanvas";

 
class Trainer extends Component {

  canvas = createRef()

  state = {
    "train": null,
  }

  handlePost = async (action, category=null) => {
    const data = await this.canvas.current.exportPaths()
    const res = await cleanAndPost(action, data, category)
    this.reset()
    this.setState({"train": JSON.stringify(res["result"])})
  }

  reset = () => {
    this.canvas.current.resetCanvas()
    this.setState({guess: null})
  }
 
  render() {
    return (
      <>
        <div className="link"><Link to={"/"}>Home</Link></div>
        <div className="center-within colored">
          <div className="top-margin">
            <MyCanvas canvas={this.canvas}/>
          </div>
          <div>
            <button className="btn-small waves-effect waves-light blue"           
            onClick={() => this.handlePost("sample", "X")}>Train X</button>
            <button className="btn-small waves-effect waves-light blue"           
            onClick={() => this.handlePost("sample", "O")}>Train O</button>
            <button className="btn-small waves-effect waves-light red" 
            onClick={() => this.reset()}>Clear</button>
            
            { this.state.train && 
            <p className="message">Thanks for submitting an {this.state.train} for training</p>}
          </div>
        </div>
      </>
    );
  }
};

export default Trainer