import React, { useEffect, useState } from 'react'
import { User as UserIcon, LogOut, Settings } from 'lucide-react'
import { Link, useNavigate } from 'react-router-dom'
import { useAppDispatch, useAppSelector } from '../../store/hooks'
import { logoutThunk, loadMe } from '../../store/slices/auth'
import Avatar from '../ui/Avatar'
import clsx from 'clsx'

const UserDropdown: React.FC = ()=>{
  const dispatch = useAppDispatch()
  const navigate = useNavigate()
  const user = useAppSelector(s=>s.auth.user)
  const [open,setOpen] = useState(false)
  useEffect(()=>{ if(!user){ dispatch(loadMe()) } }, [])
  const logout = async ()=>{
    await dispatch(logoutThunk())
    navigate('/login')
  }
  return (
    <div className='relative'>
      <button onClick={()=>setOpen(o=>!o)} className='flex items-center space-x-2 p-2 rounded hover:bg-gray-50 dark:hover:bg-gray-800'>
        <Avatar src={user?.avatar_url} name={user?.username} />
        <span className='hidden sm:block'>{user?.username || 'Account'}</span>
      </button>
      {open && (
        <div className='absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded shadow z-30'>
          <Link to='/profile' className='flex items-center gap-2 px-3 py-2 hover:bg-gray-50 dark:hover:bg-gray-700'><Settings size={16}/> Profile</Link>
          <button onClick={logout} className='w-full text-left flex items-center gap-2 px-3 py-2 hover:bg-gray-50 dark:hover:bg-gray-700'><LogOut size={16}/> Logout</button>
        </div>
      )}
    </div>
  )
}

export default UserDropdown
