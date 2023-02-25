import { useState } from "react";
import { postData } from "../utils/api";
 


const UpdateModel = () => {

  const [data, setData] = useState()

  const handleClick = (e) => {
      const d = postData("update")
      setData({"data": d["update"]})
    }
  
  return(
    <>
      <p>Update the model including the most recent data</p>
      <button onClick={handleClick}>Update</button>
      {data && <p>{data.data}</p>}
    </>
  )
}

export default UpdateModel


 
