import React, { useState } from 'react'
import { Link, NavLink } from 'react-router-dom'
import { Menu, SunMoon } from 'lucide-react'
import UserDropdown from './UserDropdown'
import clsx from 'clsx'

const Navbar: React.FC = ()=>{
  const [open, setOpen] = useState(false)
  const [dark, setDark] = useState(false)
  const toggleDark = ()=>{
    setDark(d=>!d)
    if(!dark) document.documentElement.classList.add('dark')
    else document.documentElement.classList.remove('dark')
  }
  return (
    <nav className='bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800'>
      <div className='max-w-7xl mx-auto px-4'>
        <div className='flex items-center justify-between h-16'>
          <div className='flex items-center space-x-4'>
            <button onClick={()=>setOpen(o=>!o)} className='md:hidden p-2'><Menu/></button>
            <Link to='/' className='text-xl font-semibold'>BookLMS</Link>
            <div className='hidden md:flex space-x-2'>
              <NavLink to='/' className={({isActive})=>clsx('px-3 py-2 rounded', isActive && 'bg-gray-100 dark:bg-gray-800')}>Home</NavLink>
              <NavLink to='/courses' className={({isActive})=>clsx('px-3 py-2 rounded', isActive && 'bg-gray-100 dark:bg-gray-800')}>Courses</NavLink>
            </div>
          </div>
          <div className='flex items-center space-x-3'>
            <button onClick={toggleDark} className='p-2'><SunMoon /></button>
            <UserDropdown />
          </div>
        </div>
      </div>
      {open && (
        <div className='md:hidden bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-800'>
          <div className='px-4 py-2'>
            <NavLink to='/' onClick={()=>setOpen(false)}>Home</NavLink>
          </div>
        </div>
      )}
    </nav>
  )
}

export default Navbar
