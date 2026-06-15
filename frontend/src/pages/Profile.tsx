import React from 'react'
import ProfileEdit from './ProfileEdit'
import ChangePassword from './ChangePassword'
import Sidebar from '../components/layout/Sidebar'
import Navbar from '../components/layout/Navbar'

export default function Profile(){
  return (
    <div className='min-h-screen flex flex-col'>
      <Navbar />
      <div className='flex flex-1'>
        <Sidebar />
        <main className='flex-1 p-6'>
          <h1 className='text-2xl mb-4'>My Profile</h1>
          <div className='grid grid-cols-1 lg:grid-cols-2 gap-6'>
            <ProfileEdit />
            <ChangePassword />
          </div>
        </main>
      </div>
    </div>
  )
}
