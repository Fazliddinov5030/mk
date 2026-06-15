import React from 'react'
import clsx from 'clsx'

const Modal: React.FC<{open:boolean, onClose:()=>void, title?:React.ReactNode, footer?:React.ReactNode, size?:'sm'|'md'|'lg'}> = ({open, onClose, title, footer, size='md', children})=>{
  if(!open) return null
  const sizes: Record<string,string> = {sm:'max-w-md', md:'max-w-2xl', lg:'max-w-4xl'}
  return (
    <div className='fixed inset-0 z-50 flex items-center justify-center'>
      <div className='fixed inset-0 bg-black/40' onClick={onClose} />
      <div className={clsx('bg-white dark:bg-gray-800 rounded-lg p-4 shadow-lg mx-4 w-full', sizes[size])}>
        {title && <div className='font-semibold mb-2'>{title}</div>}
        <div className='mb-4'>{children}</div>
        {footer && <div className='mt-2'>{footer}</div>}
      </div>
    </div>
  )
}

export default Modal
