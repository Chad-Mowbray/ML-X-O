import { useState } from "react";
import { postData } from "../utils/api";
import { Link } from 'react-router-dom'

 
const UpdateModel = () => {

  const [score, setData] = useState()

  const handleClick = async (e) => {
      const d = await postData("update")
      setData(d["score"])
    }
  
  return(
    <>
      <div className="link"><Link to={"/"}>Home</Link></div>
      <p>Update the model including the most recent data</p>
      <button onClick={handleClick}>Update</button>
      {score && <p>Accuracy score on newly-trained model: {score}</p>}
    </>
  )
}

export default UpdateModel


 
