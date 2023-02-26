import axios from 'axios'

const baseURL = `http://${window.location.hostname}:5000`

const api = axios.create({
  baseURL: baseURL,
})

const makeThumbnailSrc = (item) => {
  return `${baseURL}/item/thumbnail/${item.uid}`
}

export { api, makeThumbnailSrc }
