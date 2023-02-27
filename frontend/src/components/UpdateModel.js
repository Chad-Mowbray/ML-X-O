import { useState } from "react";
import { updateModelReq } from "../utils/api";
import { Link } from 'react-router-dom'
import SignupIn from "./SignupIn";

 
const UpdateModel = () => {

  const [score, setScore] = useState()
  const [token, setToken] = useState()
 
  const login = (token) => {
    setToken(token)
  }

  const handleClick = async (e) => {
      const d = await updateModelReq("update", token)
      setScore(d["score"])
    }
  
  return(
    <>
      <div className="link"><Link to={"/"}>Home</Link></div>
        { !token && <SignupIn login={login}/>}
      <div className="update">
        <p>Update the model including the most recent data</p>
        <button onClick={handleClick}>Update</button>
        {score && <p>Accuracy score on newly-trained model: {score}</p>}
      </div>
    </>
  )
}

export default UpdateModel


 
