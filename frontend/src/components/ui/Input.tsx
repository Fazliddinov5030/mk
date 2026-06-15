import React, { useState } from 'react'
import clsx from 'clsx'

interface InputProps extends React.InputHTMLAttributes<HTMLInputElement>{
  label?: string
  error?: string | null
  containerClassName?: string
}

const Input: React.FC<InputProps> = ({label, error=null, type='text', containerClassName='', className='', ...rest})=>{
  const [show, setShow] = useState(false)
  const isPassword = type === 'password'
  return (
    <div className={clsx('w-full', containerClassName)}>
      {label && <label className='block text-sm font-medium mb-1'>{label}</label>}
      <div className='relative'>
        <input
          type={isPassword ? (show ? 'text' : 'password') : type}
          className={clsx('w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-200', error ? 'border-red-400' : 'border-gray-200', className)}
          {...rest}
        />
        {isPassword && (
          <button type='button' onClick={()=>setShow(s=>!s)} className='absolute right-2 top-1/2 -translate-y-1/2 text-sm text-gray-500'>
            {show ? 'Hide' : 'Show'}
          </button>
        )}
      </div>
      {error && <p className='text-sm text-red-600 mt-1'>{error}</p>}
    </div>
  )
}

export default Input
