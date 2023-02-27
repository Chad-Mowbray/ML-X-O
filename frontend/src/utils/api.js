import { getLinesRepr } from "./processor"


const BASE_URL = process.env.REACT_APP_BASE_URL || "localhost"

const urls = {
  guess: `http://${BASE_URL}/api/guess/`,
  sample: `http://${BASE_URL}/api/provide-sample/`,
  update: `http://${BASE_URL}/api/update-model/`,
  signup: `http://${BASE_URL}/api/accounts/signup/`,
  getToken: `http://${BASE_URL}/api/accounts/get-token/`,
}

function chooseUrl(action) {
  return urls[action]
}

export async function postData(action, rawLineData=null, category=null) {
  const url = chooseUrl(action)
  const body = {rawLineData: rawLineData, category: category}
  const response = await fetch(url, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body)
  })
  const data = await response.json()
  return data
}

export async function updateModelReq(action, token) {
  const url = chooseUrl(action)
  const response = await fetch(url, {
    method: "POST",
    headers: {'Content-Type': 'application/json', "Authorization": `Token ${token}`},
    // body: JSON.stringify(body)
  })
  const data = await response.json()
  return data
}

export async function cleanAndPost(action, rawData=null, category=null){
  let rawLineData = getLinesRepr(rawData)
  const res = await postData(action, rawLineData, category)
  return res
}

export async function signUpLogIn(action, uname, pw) {
  const url = chooseUrl(action)
  const body = {username: uname, password: pw}
  const response = await fetch(url, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body)
  })
  const data = await response.json()
  return data
}

