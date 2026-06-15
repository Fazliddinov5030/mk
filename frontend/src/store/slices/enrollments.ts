import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import enrollmentService from '../../services/enrollment'

export const enrollCourse = createAsyncThunk('enrollments/enroll', async (courseId:number)=>{
  return await enrollmentService.enroll(courseId)
})

export const fetchMyCourses = createAsyncThunk('enrollments/my', async ()=>{
  return await enrollmentService.myCourses()
})

const slice = createSlice({
  name: 'enrollments',
  initialState: { list: [], loading:false, error:null },
  reducers: {},
  extraReducers: builder => {
    builder
      .addCase(enrollCourse.pending, state=>{ state.loading=true; state.error=null })
      .addCase(enrollCourse.fulfilled, (state, action)=>{ state.loading=false; state.list.push(action.payload) })
      .addCase(enrollCourse.rejected, (state, action)=>{ state.loading=false; state.error=action.error.message })
      .addCase(fetchMyCourses.pending, state=>{ state.loading=true })
      .addCase(fetchMyCourses.fulfilled, (state, action)=>{ state.loading=false; state.list=action.payload })
      .addCase(fetchMyCourses.rejected, (state, action)=>{ state.loading=false; state.error=action.error.message })
  }
})

export default slice.reducer
