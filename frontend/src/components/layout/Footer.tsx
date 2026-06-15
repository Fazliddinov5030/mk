import React from 'react'

const Footer: React.FC = ()=>{
  return (
    <footer className='mt-8 py-6 text-center text-sm text-gray-500'>
      © {new Date().getFullYear()} BookLMS. All rights reserved.
    </footer>
  )
}

export default Footer
