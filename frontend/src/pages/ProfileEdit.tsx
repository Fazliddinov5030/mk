import React, { useEffect, useState } from 'react'
import { useAppDispatch, useAppSelector } from '../store/hooks'
import profileService from '../services/profile'
import { setUser } from '../store/slices/auth'
import Input from '../components/ui/Input'
import Button from '../components/ui/Button'
import Card from '../components/ui/Card'
import Alert from '../components/ui/Alert'

export default function ProfileEdit(){
  const user = useAppSelector(s=>s.auth.user)
  const dispatch = useAppDispatch()
  const [form,setForm] = useState({username:'', email:''})
  const [loading,setLoading] = useState(false)
  const [error,setError] = useState<string|null>(null)
  const [success,setSuccess] = useState<string|null>(null)
  useEffect(()=>{ if(user) setForm({username:user.username||'', email:user.email||''}) }, [user])
  const submit = async (e:any)=>{
    e.preventDefault(); setLoading(true); setError(null); setSuccess(null)
    try{
      const updated = await profileService.updateProfile(form)
      dispatch(setUser(updated))
      setSuccess('Profile updated')
    }catch(err:any){ setError(err?.response?.data?.detail || err?.message || 'Update failed') }
    finally{ setLoading(false) }
  }
  return (
    <div className='p-6'>
      <Card title='Edit Profile' className='max-w-lg'>
        {error && <Alert variant='error'>{error}</Alert>}
        {success && <Alert variant='success'>{success}</Alert>}
        <form onSubmit={submit} className='space-y-3 mt-3'>
          <Input label='Username' value={form.username} onChange={e=>setForm({...form, username:e.target.value})} />
          <Input label='Email' value={form.email} onChange={e=>setForm({...form, email:e.target.value})} />
          <Button loading={loading} type='submit'>Save</Button>
        </form>
      </Card>
    </div>
  )
}
