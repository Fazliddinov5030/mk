import React, { useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { useAppDispatch, useAppSelector } from '../store/hooks'
import { fetchCourseDetail } from '../store/slices/courses'
import CourseCard from '../components/CourseCard'
import enrollmentService from '../services/enrollment'
import { enrollCourse } from '../store/slices/enrollments'

const CourseDetail: React.FC = ()=>{
  const { slug } = useParams<{slug:string}>()
  const dispatch = useAppDispatch()
  const { detail, loading } = useAppSelector(s=>s.courses)

  useEffect(()=>{
    if(slug) dispatch(fetchCourseDetail(slug))
  },[slug, dispatch])

  const onEnroll = async () => {
    if(!detail) return
    dispatch(enrollCourse(detail.id))
  }

  if(loading || !detail) return <div>Loading...</div>

  return (
    <div className='container mx-auto py-8'>
      <div className='grid md:grid-cols-3 gap-6'>
        <div className='md:col-span-2'>
          <h1 className='text-2xl font-bold'>{detail.title}</h1>
          <p className='mt-2 text-gray-700'>{detail.description}</p>

          <div className='mt-6'>
            <h3 className='text-lg font-semibold'>Lessons</h3>
            <ul className='mt-2'>
              {detail.modules?.map((m:any)=> (
                <li key={m.id} className='mb-2'>
                  <div className='font-medium'>{m.title}</div>
                  <ul className='ml-4'>
                    {m.lessons?.map((l:any)=>(<li key={l.id}>{l.title}</li>))}
                  </ul>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <aside>
          <div className='p-4 border rounded'>
            <div className='text-sm text-gray-600'>Instructor</div>
            <div className='font-medium'>{detail.instructor?.username}</div>
            <div className='mt-4'>
              <button onClick={onEnroll} className='w-full px-4 py-2 bg-blue-600 text-white rounded'>Enroll</button>
            </div>
          </div>
        </aside>
      </div>

      <div className='mt-8'>
        <h3 className='text-lg font-semibold'>Related Courses</h3>
        <div className='grid grid-cols-1 gap-4 mt-3'>
          {detail.related?.map((r:any)=>(<CourseCard key={r.id} course={r} />))}
        </div>
      </div>
    </div>
  )
}

export default CourseDetail
import React, { useEffect, useState } from 'react'
import api from '../services/api'
import { useParams } from 'react-router-dom'
import Card from '../components/ui/Card'
import { PageLoader } from '../components/ui/Loader'

export default function CourseDetail(){
  const { slug } = useParams()
  const [course,setCourse] = useState<any>(null)
  const [loading,setLoading] = useState(false)
  const [error,setError] = useState<string|null>(null)
  useEffect(()=>{
    setLoading(true)
    api.get(`/api/courses/${slug}/`).then(r=>setCourse(r.data)).catch(e=>setError(e?.message || 'Not found')).finally(()=>setLoading(false))
  },[slug])
  if(loading) return <PageLoader />
  if(error) return <Card><p className='text-red-600'>{error}</p></Card>
  if(!course) return <Card><p>Course not found</p></Card>
  return (
    <div className='p-6'>
      <Card title={course.title}>
        <p className='text-sm text-gray-600'>{course.description}</p>
      </Card>
    </div>
  )
}
