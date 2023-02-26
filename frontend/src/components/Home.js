import {Component} from 'react'
import { Link } from 'react-router-dom'


const Home = () => {
    return(
      <div >
        <div className="link"><Link to={"/training-data"}>Provide training data to the model</Link></div>
        <div className="link"><Link to={"/guess"}>Test out the model</Link></div>
        <div className="link"><Link to={"/update-model"}>Update the model to include new training data</Link></div>
      </div>
    )
}

export default Home