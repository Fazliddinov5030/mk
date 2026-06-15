import React from 'react'
import { Link } from 'react-router-dom'
import Card from './ui/Card'

const CourseCard: React.FC<{course:any}> = ({course}) =>{
  return (
    <Card className='hover:shadow-md'>
      <div className='flex flex-col md:flex-row gap-4'>
        {course.image && <img src={course.image} alt={course.title} className='w-full md:w-40 h-28 object-cover rounded' />}
        <div className='flex-1'>
          <h3 className='text-lg font-semibold'><Link to={`/courses/${course.slug}`}>{course.title}</Link></h3>
          <p className='text-sm text-gray-600'>{course.short_description}</p>
          <div className='mt-2 text-sm text-gray-500'>By {course.instructor?.username}</div>
        </div>
      </div>
    </Card>
  )
}

export default CourseCard
