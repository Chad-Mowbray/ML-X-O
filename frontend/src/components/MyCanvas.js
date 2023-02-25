import { ReactSketchCanvas } from "react-sketch-canvas";
import {Component} from "react";

 
class MyCanvas extends Component {
 
  render() {
    return (
      <ReactSketchCanvas
      ref={this.props.canvas}
      strokeWidth={10}
      strokeColor="black"
      width="99px"
      height="99px"/>
    )
  }
}

export default MyCanvas

