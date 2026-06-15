import React from 'react'
import clsx from 'clsx'

interface CardProps extends React.HTMLAttributes<HTMLDivElement>{
  title?: React.ReactNode
  footer?: React.ReactNode
}

const Card: React.FC<CardProps> = ({title, footer, children, className='', ...rest})=>{
  return (
    <div className={clsx('bg-white dark:bg-gray-800 rounded-lg shadow p-4', className)} {...rest}>
      {title && <div className='mb-2 text-lg font-semibold'>{title}</div>}
      <div>{children}</div>
      {footer && <div className='mt-4 text-sm text-gray-500'>{footer}</div>}
    </div>
  )
}

export default Card
