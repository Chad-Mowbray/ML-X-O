import {Component, createRef} from "react";
import { Link } from 'react-router-dom'
import { cleanAndPost } from "../utils/api";
import MyCanvas from "./MyCanvas";

class Guess extends Component {
  
  canvas = createRef()

  state = {
    "guess": null,
  }


  handlePost = async (action, category=null) => {
    const data = await this.canvas.current.exportPaths()
    const res = await cleanAndPost(action, data, category)
    this.reset()
    this.setState({"guess": res["best_guess"]})
  }

  reset = () => {
    this.canvas.current.resetCanvas()
    this.setState({guess: null})
  }

  getMessage = () => {
    if (this.state.guess === "NONE") {
      return <Link to="/training-data">The model has not been trained yet.</Link>
    } else {
      return`You probably drew an ${this.state.guess}`
    }
  }

 
  render() {
    return (
      <>
        <div className="link"><Link to={"/"}>Home</Link></div>
        <div className="center-within colored">
          <div className="top-margin">
            <MyCanvas canvas={this.canvas}/>
          </div>
          <button className="btn-small waves-effect waves-light" 
            onClick={() => this.handlePost("guess")}>Guess</button>
          <button className="btn-small waves-effect waves-light red" 
          onClick= {() => this.reset()}>Clear</button>
            
          { this.state.guess && 
          <p className="message">{this.getMessage()}</p>}
        </div>
      </>
    );
  }
};

export default Guess