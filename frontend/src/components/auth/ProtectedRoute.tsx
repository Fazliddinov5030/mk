import React from 'react'
import { Navigate, useLocation } from 'react-router-dom'

const ProtectedRoute: React.FC<{children: React.ReactElement}> = ({children})=>{
  const token = localStorage.getItem('access')
  const location = useLocation()
  if(!token) return <Navigate to='/login' state={{from: location}} replace />
  return children
}

export default ProtectedRoute
