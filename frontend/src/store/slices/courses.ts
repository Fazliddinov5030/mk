import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import coursesService from '../../services/courses'

export const fetchCourses = createAsyncThunk('courses/fetch', async (params:any) => {
  return await coursesService.list(params)
})

export const fetchCourseDetail = createAsyncThunk('courses/detail', async (slug:string) => {
  return await coursesService.detail(slug)
})

const slice = createSlice({
  name: 'courses',
  initialState: { list: [], total:0, detail: null, loading:false, error:null },
  reducers: {},
  extraReducers: builder => {
    builder
      .addCase(fetchCourses.pending, state=>{ state.loading=true; state.error=null })
      .addCase(fetchCourses.fulfilled, (state, action)=>{ state.loading=false; state.list=action.payload; })
      .addCase(fetchCourses.rejected, (state, action)=>{ state.loading=false; state.error=action.error.message })
      .addCase(fetchCourseDetail.pending, state=>{ state.loading=true })
      .addCase(fetchCourseDetail.fulfilled, (state, action)=>{ state.loading=false; state.detail=action.payload })
      .addCase(fetchCourseDetail.rejected, (state, action)=>{ state.loading=false; state.error=action.error.message })
  }
})

export default slice.reducer
