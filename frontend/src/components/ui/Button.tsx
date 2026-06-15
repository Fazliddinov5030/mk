import React from 'react'
import clsx from 'clsx'

type Variant = 'primary'|'secondary'|'danger'|'outline'

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement>{
  variant?: Variant
  loading?: boolean
}

const variantStyles: Record<Variant,string> = {
  primary: 'bg-blue-600 hover:bg-blue-700 text-white',
  secondary: 'bg-gray-600 hover:bg-gray-700 text-white',
  danger: 'bg-red-600 hover:bg-red-700 text-white',
  outline: 'border border-gray-300 text-gray-700 bg-transparent hover:bg-gray-50'
}

const Button: React.FC<ButtonProps> = ({variant='primary', loading=false, className='', children, disabled, ...rest})=>{
  return (
    <button
      className={clsx('inline-flex items-center justify-center px-4 py-2 rounded shadow-sm transition disabled:opacity-50', variantStyles[variant], className)}
      disabled={disabled || loading}
      {...rest}
    >
      {loading && (
        <svg className='animate-spin h-4 w-4 mr-2 text-white' xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24'>
          <circle className='opacity-25' cx='12' cy='12' r='10' stroke='currentColor' strokeWidth='4'></circle>
          <path className='opacity-75' fill='currentColor' d='M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z'></path>
        </svg>
      )}
      <span>{children}</span>
    </button>
  )
}

export default Button
