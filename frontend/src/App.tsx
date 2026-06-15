import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/auth/Login'
import Register from './pages/auth/Register'
import Dashboard from './pages/Dashboard'
import Profile from './pages/Profile'
import CourseList from './pages/CourseList'
import CourseDetail from './pages/CourseDetail'
import PrivateRoute from './components/PrivateRoute'
import ProtectedRoute from './components/auth/ProtectedRoute'

export default function App(){
  return (
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/login' element={<Login/>} />
      <Route path='/register' element={<Register/>} />
      <Route path='/courses' element={<CourseList/>} />
      <Route path='/courses/:slug' element={<CourseDetail/>} />
      <Route path='/dashboard' element={<ProtectedRoute><Dashboard/></ProtectedRoute>} />
      <Route path='/profile' element={<ProtectedRoute><Profile/></ProtectedRoute>} />
    </Routes>
  )
}
