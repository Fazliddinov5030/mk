import React from 'react'

const Avatar: React.FC<{src?:string|null, name?:string, size?:number}> = ({src, name, size=32})=>{
  if(src) return <img src={src} alt={name} className='rounded-full' style={{width:size, height:size, objectFit:'cover'}} />
  const initials = (name||'U').split(' ').map(n=>n[0]).slice(0,2).join('').toUpperCase()
  return <div className='rounded-full bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-100 flex items-center justify-center' style={{width:size, height:size}}>{initials}</div>
}

export default Avatar
