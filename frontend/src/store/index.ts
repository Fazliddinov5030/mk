import { configureStore } from '@reduxjs/toolkit'
import authReducer from './slices/auth'
import coursesReducer from './slices/courses'
import enrollmentsReducer from './slices/enrollments'

export const store = configureStore({
  reducer: {
    auth: authReducer,
    courses: coursesReducer,
    enrollments: enrollmentsReducer,
  }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
