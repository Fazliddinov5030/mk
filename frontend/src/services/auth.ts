import api from './api'

const login = async (data:any)=>{
  const res = await api.post('/api/token/', data)
  const user = await api.get('/api/accounts/me/')
  return { access: res.data.access, refresh: res.data.refresh, user: user.data }
}

const register = async (data:any)=>{
  const res = await api.post('/api/accounts/register/', data)
  return res.data
}

const refresh = async ()=>{
  const refresh = localStorage.getItem('refresh')
  const res = await api.post('/api/token/refresh/', { refresh })
  return res.data
}

const logout = async ()=>{
  // If backend supports logout or token blacklist, call it. otherwise client-side only.
  try{ await api.post('/api/accounts/logout/') }catch(e){}
}

export default { login, register, refresh }
