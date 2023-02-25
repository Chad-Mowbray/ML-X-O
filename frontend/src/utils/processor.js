

export function preProcess(data) {
  let cleaned =  data.map( line => line.paths.map(point => [Math.floor(Math.round(point.x * 100 ) / 100), Math.floor(Math.round(point.y * 100) / 100)] ))
  return cleaned
}

