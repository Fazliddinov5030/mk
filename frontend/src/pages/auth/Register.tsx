import React, { useState } from 'react'
import { useAppDispatch } from '../../store/hooks'
import { register } from '../../store/slices/auth'
import { useNavigate, Link } from 'react-router-dom'
import Input from '../../components/ui/Input'
import Button from '../../components/ui/Button'
import Card from '../../components/ui/Card'
import Alert from '../../components/ui/Alert'

export default function Register(){
  const [form,setForm] = useState({username:'',password:''})
  const [error,setError] = useState<string|null>(null)
  const [loading,setLoading] = useState(false)
  const dispatch = useAppDispatch()
  const nav = useNavigate()
  const submit = async (e:any)=>{
    e.preventDefault()
    setError(null)
    setLoading(true)
    try{
      await dispatch(register(form)).unwrap()
      nav('/login')
    }catch(err:any){
      setError(err?.message || 'Registration failed')
    }finally{setLoading(false)}
  }
  return (
    <div className='min-h-screen flex items-center justify-center p-4'>
      <Card className='w-full max-w-md'>
        <h2 className='text-xl mb-4'>Register</h2>
        {error && <Alert variant='error'>{error}</Alert>}
        <form onSubmit={submit} className='space-y-3 mt-3'>
          <Input label='Username' value={form.username} onChange={e=>setForm({...form, username:e.target.value})} name='username' />
          <Input label='Password' type='password' value={form.password} onChange={e=>setForm({...form, password:e.target.value})} name='password' />
          <Button type='submit' loading={loading} className='w-full'>Register</Button>
        </form>
        <div className='mt-4 text-sm'>Already have an account? <Link to='/login' className='text-blue-600'>Login</Link></div>
      </Card>
    </div>
  )
}
