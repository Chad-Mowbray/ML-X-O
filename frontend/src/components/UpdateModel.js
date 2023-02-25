import { useState } from "react";
import { postData } from "../utils/api";
 


const UpdateModel = () => {

  const [score, setData] = useState()

  const handleClick = async (e) => {
      const d = await postData("update")
      setData(JSON.stringify(d["score"]))
    }
  
  return(
    <>
      <p>Update the model including the most recent data</p>
      <button onClick={handleClick}>Update</button>
      {score && <p>Accuracy score on newly-trained model: {score}</p>}
    </>
  )
}

export default UpdateModel


 
