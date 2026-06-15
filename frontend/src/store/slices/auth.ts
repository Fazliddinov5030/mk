import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import authService from '../../services/auth'
import profileService from '../../services/profile'

const initialState = {
  user: null,
  access: null,
  refresh: null,
  loading: false,
  error: null,
}

export const login = createAsyncThunk('auth/login', async (data, thunkAPI) => {
  return authService.login(data)
})

export const register = createAsyncThunk('auth/register', async (data, thunkAPI) => {
  return authService.register(data)
})

export const refreshToken = createAsyncThunk('auth/refresh', async (_, thunkAPI) => {
  return authService.refresh()
})

export const loadMe = createAsyncThunk('auth/loadMe', async (_, thunkAPI) => {
  const user = await profileService.getProfile()
  return user
})

export const logoutThunk = createAsyncThunk('auth/logout', async (_, thunkAPI)=>{
  // try server-side logout if available
  try{ await authService.logout() }catch(e){}
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  return true
})

const slice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    setUser(state, action){ state.user = action.payload }
    logout(state){
      state.user = null
      state.access = null
      state.refresh = null
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(login.pending, (state)=>{ state.loading=true; state.error=null })
      .addCase(login.fulfilled, (state, action)=>{ state.loading=false; state.access=action.payload.access; state.refresh=action.payload.refresh; state.user=action.payload.user; localStorage.setItem('access', action.payload.access); localStorage.setItem('refresh', action.payload.refresh) })
      .addCase(login.rejected, (state, action)=>{ state.loading=false; state.error = action.error.message })
      .addCase(register.pending, (state)=>{ state.loading=true })
      .addCase(register.fulfilled, (state, action)=>{ state.loading=false })
      .addCase(register.rejected, (state, action)=>{ state.loading=false; state.error = action.error.message })
      .addCase(refreshToken.fulfilled, (state, action)=>{ state.access = action.payload.access; localStorage.setItem('access', action.payload.access) })
      .addCase(loadMe.fulfilled, (state, action)=>{ state.user = action.payload })
      .addCase(logoutThunk.fulfilled, (state)=>{ state.user=null; state.access=null; state.refresh=null })
  }
})

export const { logout, setUser } = slice.actions
export default slice.reducer
