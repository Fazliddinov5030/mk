import api from './api'

const list = async (params:any) => {
  const res = await api.get('/api/courses/', { params })
  return res.data
}

const detail = async (slug:string) => {
  const res = await api.get(`/api/courses/${slug}/`)
  return res.data
}

const related = async (courseId:number) => {
  const res = await api.get(`/api/courses/`, { params: { related_to: courseId } })
  return res.data
}

export default { list, detail, related }
