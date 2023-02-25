import {Component} from 'react'
import { Link } from 'react-router-dom'


class Home extends Component {

  render() {
    return(
      <div >
        <h3>Graphical Search</h3>
          <h5>Draw an "X" or an "O" with your mouse, and I will try to guess which one you drew:</h5>
          <h6>Note: the first use will take around 10 seconds</h6>
          <Link to={"/training-data"}>Provide training data to the model</Link>
          <br/>
          <Link to={"/guess"}>Test out the model</Link>
          <br/>
          <Link to={"/update-model"}>Update the model to unclude new training data</Link>
      </div>
    )
  }
}

export default Home