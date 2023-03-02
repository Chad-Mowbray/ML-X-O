import { ReactSketchCanvas } from "react-sketch-canvas";

 
const MyCanvas = ({canvas}) => {
    return (
      <ReactSketchCanvas
      ref={canvas}
      strokeWidth={10}
      strokeColor="black"
      width="99px"
      height="99px"/>
    )
}

export default MyCanvas

