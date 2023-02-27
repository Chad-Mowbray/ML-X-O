import { useState } from 'react'
import { signUpLogIn } from '../utils/api'


const SignupIn = ({login}) => {

  const [uname, setUname] = useState("")
  const [pw, setPw] = useState("")
  const [next, setNext] = useState("")

  const handleUnameChange = (e) => setUname(e.target.value)
  const handlePwChange = (e) => setPw(e.target.value)
  const handleSignup = async (e) => {
    const res = await signUpLogIn("signup", uname, pw)
    console.log(res)
    if(res.username && res.password) {
      setNext("next")
      clear()
    }

  }
  const handleLogin = async (e) => {
    const res = await signUpLogIn("getToken", uname, pw)
    login(res.token)
    clear()
  }

  const clear = () => {
    setUname("")
    setPw("")
  }

  return(
      <div className='signupin'>
        <label>
          Username:
          <input type="text" value={uname} onChange={handleUnameChange} />
        </label>
        <label>
          Password:
          <input type="password" value={pw} onChange={handlePwChange} />
        </label>
        <button className="logBtn" onClick={handleSignup}>Sign up</button>
        <button className={`logBtn ${next}`} onClick={handleLogin}>Log in</button>
      </div>
        )
}

export default SignupIn