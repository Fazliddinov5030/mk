import React from 'react'

export const Loader: React.FC<{className?:string}> = ({className=''}) => (
  <svg className={`animate-spin h-6 w-6 text-blue-600 ${className}`} xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24'>
    <circle className='opacity-25' cx='12' cy='12' r='10' stroke='currentColor' strokeWidth='4'></circle>
    <path className='opacity-75' fill='currentColor' d='M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z'></path>
  </svg>
)

export const PageLoader: React.FC = ()=> (
  <div className='fixed inset-0 flex items-center justify-center bg-white/70 dark:bg-black/50 z-50'>
    <Loader className='h-12 w-12' />
  </div>
)

export default Loader
