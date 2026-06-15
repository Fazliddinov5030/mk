import React, { useState } from 'react'
import profileService from '../services/profile'
import Card from '../components/ui/Card'
import Input from '../components/ui/Input'
import Button from '../components/ui/Button'
import Alert from '../components/ui/Alert'

export default function ChangePassword(){
  const [form,setForm] = useState({old_password:'', new_password:''})
  const [loading,setLoading] = useState(false)
  const [error,setError] = useState<string|null>(null)
  const [success,setSuccess] = useState<string|null>(null)
  const submit = async (e:any)=>{
    e.preventDefault(); setLoading(true); setError(null); setSuccess(null)
    try{
      await profileService.changePassword(form.old_password, form.new_password)
      setSuccess('Password changed successfully')
      setForm({old_password:'', new_password:''})
    }catch(err:any){ setError(err?.response?.data?.detail || err?.message || 'Change password failed') }
    finally{ setLoading(false) }
  }
  return (
    <div className='p-6'>
      <Card title='Change password' className='max-w-md'>
        {error && <Alert variant='error'>{error}</Alert>}
        {success && <Alert variant='success'>{success}</Alert>}
        <form onSubmit={submit} className='space-y-3 mt-3'>
          <Input label='Current password' type='password' value={form.old_password} onChange={e=>setForm({...form, old_password:e.target.value})} />
          <Input label='New password' type='password' value={form.new_password} onChange={e=>setForm({...form, new_password:e.target.value})} />
          <Button loading={loading} type='submit'>Change password</Button>
        </form>
      </Card>
    </div>
  )
}
