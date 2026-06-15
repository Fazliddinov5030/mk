import React, { useEffect, useState } from 'react'
import { useAppDispatch, useAppSelector } from '../store/hooks'
import { fetchCourses } from '../store/slices/courses'
import CourseCard from '../components/CourseCard'
import Pagination from '../components/Pagination'

const CourseList: React.FC = ()=>{
  const dispatch = useAppDispatch()
  const { list, loading } = useAppSelector(s=>s.courses)
  // API returns paginated object sometimes; normalize
  const courses = Array.isArray(list) ? list : (list.results || [])
  const total = Array.isArray(list) ? list.length : (list.count || 0)
  const [page,setPage] = useState(1)
  const [q,setQ] = useState('')

  useEffect(()=>{
    dispatch(fetchCourses({ page, q }))
  },[dispatch, page, q])

  return (
    <div className='container mx-auto py-8'>
      <div className='flex items-center mb-4'>
        <input value={q} onChange={e=>setQ(e.target.value)} placeholder='Search courses...' className='flex-1 border p-2 rounded' />
      </div>

      {loading && <div>Loading...</div>}

      <div className='grid grid-cols-1 gap-4'>
        {courses.map((c:any)=> <CourseCard key={c.id} course={c} />)}
      </div>

      <div className='mt-6'>
        <Pagination page={page} total={total} perPage={10} onPage={setPage} />
      </div>
    </div>
  )
}

export default CourseList
import React, { useEffect, useState } from 'react'
import api from '../services/api'
import { Link } from 'react-router-dom'
import Card from '../components/ui/Card'
import Loader, { PageLoader } from '../components/ui/Loader'
import Alert from '../components/ui/Alert'

export default function CourseList(){
  const [courses,setCourses] = useState<any[]>([])
  const [loading,setLoading] = useState(false)
  const [error,setError] = useState<string|null>(null)
  useEffect(()=>{
    setLoading(true)
    api.get('/api/courses/').then(r=>setCourses(r.data)).catch(e=>setError(e?.message || 'Failed to load')).finally(()=>setLoading(false))
  },[])
  if(loading) return <PageLoader />
  return (
    <div className='p-6'>
      <h1 className='text-2xl'>Courses</h1>
      {error && <Alert variant='error'>{error}</Alert>}
      <div className='mt-4 grid grid-cols-1 md:grid-cols-2 gap-4'>
        {courses.map(c=> (
          <Card key={c.id} title={c.title} className='hover:shadow-md'>
            <p className='text-sm text-gray-600'>{c.short_description || c.description}</p>
            <div className='mt-3'>
              <Link to={`/courses/${c.slug}`} className='text-blue-600 underline'>View course</Link>
            </div>
          </Card>
        ))}
      </div>
    </div>
  )
}
