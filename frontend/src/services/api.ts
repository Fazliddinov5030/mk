import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_URL,
  headers: { 'Content-Type': 'application/json' }
})

api.interceptors.request.use((cfg)=>{
  const token = localStorage.getItem('access')
  if(token) cfg.headers!['Authorization'] = `Bearer ${token}`
  return cfg
})

api.interceptors.response.use((res)=>res, async (err)=>{
  const original = err.config
  if(err.response && err.response.status === 401 && !original._retry){
    original._retry = true
    const refresh = localStorage.getItem('refresh')
    if(refresh){
      const r = await axios.post(`${API_URL}/api/token/refresh/`, { refresh })
      localStorage.setItem('access', r.data.access)
      err.config.headers['Authorization'] = `Bearer ${r.data.access}`
      return axios(original)
    }
  }
  return Promise.reject(err)
})

export default api
