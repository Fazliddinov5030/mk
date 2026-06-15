import React from 'react'
import { NavLink } from 'react-router-dom'
import { Home, Book, User } from 'lucide-react'

const Sidebar: React.FC<{className?:string}> = ({className=''})=>{
  return (
    <aside className={`w-64 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 p-4 ${className}`}>
      <nav className='space-y-1'>
        <NavLink to='/' className={({isActive})=>`flex items-center p-2 rounded ${isActive ? 'bg-gray-100 dark:bg-gray-800' : 'hover:bg-gray-50 dark:hover:bg-gray-800'}`}><Home className='mr-2'/> Home</NavLink>
        <NavLink to='/courses' className={({isActive})=>`flex items-center p-2 rounded ${isActive ? 'bg-gray-100 dark:bg-gray-800' : 'hover:bg-gray-50 dark:hover:bg-gray-800'}`}><Book className='mr-2'/> Courses</NavLink>
        <NavLink to='/profile' className={({isActive})=>`flex items-center p-2 rounded ${isActive ? 'bg-gray-100 dark:bg-gray-800' : 'hover:bg-gray-50 dark:hover:bg-gray-800'}`}><User className='mr-2'/> Profile</NavLink>
      </nav>
    </aside>
  )
}

export default Sidebar
