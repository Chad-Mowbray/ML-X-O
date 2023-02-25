import React from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";
 
 
export const getCanvas = () => {
  return (
    <ReactSketchCanvas
    ref={this.canvas}
    strokeWidth={10}
    strokeColor="black"
    width="99px"
    height="99px"/>
  )
}