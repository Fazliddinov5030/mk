import React, { useState } from 'react'
import { useAppDispatch } from '../../store/hooks'
import { login } from '../../store/slices/auth'
import { useNavigate, useLocation, Link } from 'react-router-dom'
import Input from '../../components/ui/Input'
import Button from '../../components/ui/Button'
import Card from '../../components/ui/Card'
import Alert from '../../components/ui/Alert'

export default function Login(){
  const [form,setForm] = useState({username:'',password:''})
  const [error,setError] = useState<string|null>(null)
  const [loading,setLoading] = useState(false)
  const dispatch = useAppDispatch()
  const nav = useNavigate()
  const location = useLocation()
  const from = (location.state as any)?.from?.pathname || '/dashboard'
  const submit = async (e:any)=>{
    e.preventDefault()
    setError(null)
    setLoading(true)
    try{
      await dispatch(login(form)).unwrap()
      nav(from)
    }catch(err:any){
      setError(err?.message || 'Login failed')
    }finally{setLoading(false)}
  }
  return (
    <div className='min-h-screen flex items-center justify-center p-4'>
      <Card className='w-full max-w-md'>
        <h2 className='text-xl mb-4'>Login</h2>
        {error && <Alert variant='error'>{error}</Alert>}
        <form onSubmit={submit} className='space-y-3 mt-3'>
          <Input label='Username' value={form.username} onChange={e=>setForm({...form, username:e.target.value})} name='username' />
          <Input label='Password' type='password' value={form.password} onChange={e=>setForm({...form, password:e.target.value})} name='password' />
          <Button type='submit' loading={loading} className='w-full'>Login</Button>
        </form>
        <div className='mt-4 text-sm'>Don't have an account? <Link to='/register' className='text-blue-600'>Register</Link></div>
      </Card>
    </div>
  )
}
