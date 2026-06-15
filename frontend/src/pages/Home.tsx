import React from 'react'
import { Link } from 'react-router-dom'

export default function Home(){
  return (
    <div className='p-6'>
      <h1 className='text-2xl'>Welcome to Book LMS</h1>
      <div className='mt-4'>
        <Link to='/courses' className='text-blue-600 underline'>Browse Courses</Link>
      </div>
    </div>
  )
}
