
const BASE_URL = process.env.REACT_APP_BASE_URL || "localhost"

const urls = {
  guess: `http://${BASE_URL}/api/guess/`,
  sample: `http://${BASE_URL}/api/provide-sample/`
}

function chooseUrl(key) {
  return urls[key]
}


export async function postData(processedData, action, category=null) {
  const url = chooseUrl(action)
  console.log(url)
  const body = {data: processedData, category: category}
  const response = await fetch(url, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body)
  })
  const data = await response.json()
  return data
}