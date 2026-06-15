import React, { useEffect } from 'react'
import { createRoot } from 'react-dom/client'
import { Provider } from 'react-redux'
import { BrowserRouter } from 'react-router-dom'
import App from './App'
import { store } from './store'
import { loadMe } from './store/slices/auth'
import './styles/index.css'

const Root = () =>{
  useEffect(()=>{
    const token = localStorage.getItem('access')
    if(token) store.dispatch(loadMe())
  }, [])
  return (
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  )
}

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>
)
