// lightweight smoke test placeholder for ProtectedRoute usage example
import React from 'react'
import { render } from '@testing-library/react'
import ProtectedRoute from './ProtectedRoute'

test('renders children when token present', ()=>{
  localStorage.setItem('access','token')
  const { container } = render(<ProtectedRoute><div>ok</div></ProtectedRoute>)
  expect(container.textContent).toContain('ok')
  localStorage.removeItem('access')
})
