import { getLinesRepr } from "./processor"


const BASE_URL = process.env.REACT_APP_BASE_URL || "localhost"

const urls = {
  guess: `http://${BASE_URL}/api/guess/`,
  sample: `http://${BASE_URL}/api/provide-sample/`,
  update: `http://${BASE_URL}/api/update-model/`
}

function chooseUrl(action) {
  return urls[action]
}

export async function postData(action, rawLineData=null, category=null) {
  const url = chooseUrl(action)
  console.log(url)
  const body = {rawLineData: rawLineData, category: category}
  console.log("body", body)
  const response = await fetch(url, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body)
  })
  const data = await response.json()
  return data
}

export async function cleanAndPost(action, rawData=null, category=null){
  console.log("raw data: ", rawData)
  let rawLineData = getLinesRepr(rawData)
  console.log("cleaned: ", rawLineData)
  const res = await postData(action, rawLineData, category)
  console.log("res: ", res)
  return res
}