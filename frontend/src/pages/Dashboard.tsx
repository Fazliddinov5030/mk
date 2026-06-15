import React from 'react'
import Sidebar from '../components/layout/Sidebar'
import Navbar from '../components/layout/Navbar'
import Footer from '../components/layout/Footer'
import Card from '../components/ui/Card'

export default function Dashboard(){
  return (
    <div className='min-h-screen flex flex-col'>
      <Navbar />
      <div className='flex flex-1'>
        <Sidebar />
        <main className='flex-1 p-6'>
          <h1 className='text-2xl mb-4'>Dashboard</h1>
          <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'>
            <Card title='Overview'>Stats and charts go here</Card>
            <Card title='Recent Activity'>Recent activity list</Card>
            <Card title='Quick Actions'>Links and actions</Card>
          </div>
          <Footer />
        </main>
      </div>
    </div>
  )
}
