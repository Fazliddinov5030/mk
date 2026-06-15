import React from 'react'

const Pagination: React.FC<{page:number, total:number, perPage:number, onPage:(p:number)=>void}> = ({page, total, perPage, onPage})=>{
  const pages = Math.ceil(total / perPage)
  if(pages <= 1) return null
  return (
    <div className='flex items-center space-x-2'>
      <button disabled={page<=1} onClick={()=>onPage(page-1)} className='px-3 py-1 border rounded'>Prev</button>
      {[...Array(pages)].map((_,i)=> (
        <button key={i} onClick={()=>onPage(i+1)} className={`px-3 py-1 rounded ${i+1===page? 'bg-blue-600 text-white' : 'border'}`}>{i+1}</button>
      ))}
      <button disabled={page>=pages} onClick={()=>onPage(page+1)} className='px-3 py-1 border rounded'>Next</button>
    </div>
  )
}

export default Pagination
