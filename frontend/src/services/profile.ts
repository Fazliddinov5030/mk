import api from './api'

const getProfile = async ()=>{
  const res = await api.get('/api/accounts/me/')
  return res.data
}

const updateProfile = async (data:any)=>{
  const res = await api.patch('/api/accounts/me/', data)
  return res.data
}

const changePassword = async (oldPassword:string, newPassword:string)=>{
  // Backend may not have this endpoint; call it if available
  const res = await api.post('/api/accounts/change_password/', { old_password: oldPassword, new_password: newPassword })
  return res.data
}

export default { getProfile, updateProfile, changePassword }
