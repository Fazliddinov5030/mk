import React from 'react'
import clsx from 'clsx'
import { CheckCircle, AlertTriangle, Info, XCircle } from 'lucide-react'

type Variant = 'success'|'warning'|'error'|'info'

const icons: Record<Variant, any> = {
  success: CheckCircle,
  warning: AlertTriangle,
  error: XCircle,
  info: Info,
}

const colors: Record<Variant,string> = {
  success: 'bg-green-50 border-green-200 text-green-800',
  warning: 'bg-yellow-50 border-yellow-200 text-yellow-800',
  error: 'bg-red-50 border-red-200 text-red-800',
  info: 'bg-blue-50 border-blue-200 text-blue-800',
}

const Alert: React.FC<{variant?:Variant, children:React.ReactNode, className?:string}> = ({variant='info', children, className=''})=>{
  const Icon = icons[variant]
  return (
    <div className={clsx('rounded-md p-3 border flex items-start space-x-3', colors[variant], className)} role='alert'>
      <div className='mt-0.5'><Icon size={20} /></div>
      <div className='text-sm'>{children}</div>
    </div>
  )
}

export default Alert
