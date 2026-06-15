import api from './api'

const enroll = async (courseId:number) => {
  const res = await api.post('/api/enrollments/enroll/', { course_id: courseId })
  return res.data
}

const myCourses = async () => {
  const res = await api.get('/api/enrollments/my_courses/')
  return res.data
}

const progress = async (enrollmentId:number, payload:any) => {
  const res = await api.post(`/api/enrollments/${enrollmentId}/progress/`, payload)
  return res.data
}

export default { enroll, myCourses, progress }
