import React from 'react';

// TypeScript interface
interface Course {
  id: number;
  title: string;
  description: string;
  price: number | null;
}

export default async function HomePage() {
  // Django REST Framework API'dan ma'lumot olish (Server-Side Rendering)
  // Sizning API yo'lingiz boshqacha bo'lsa, moslashtiring:
  let courses: Course[] = [];
  try {
    const res = await fetch('http://127.0.0.1:8000/api/courses/', { cache: 'no-store' });
    if (res.ok) {
      courses = await res.json();
    }
  } catch (error) {
    console.error("API ga ulanishda xatolik:", error);
  }

  return (
    <div className="min-h-screen bg-slate-50 py-12 px-6 font-sans">
      <div className="max-w-7xl mx-auto">
        <div className="mb-10 text-center md:text-left">
          <h1 className="text-4xl font-bold text-slate-900 mb-4 tracking-tight">Eng so'nggi kurslar</h1>
          <p className="text-lg text-slate-500">O'zingizga mos kursni tanlang va kelajagingiz sari ilk qadamni tashlang.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {courses.map((course) => (
            <div key={course.id} className="bg-white rounded-2xl border border-slate-100 shadow-sm hover:shadow-lg transition-all duration-300 flex flex-col overflow-hidden group">
              <div className="w-full h-52 bg-slate-100 flex items-center justify-center text-slate-400 group-hover:bg-slate-200 transition-colors">
                <span className="text-sm font-medium">Rasm (Placeholder)</span>
              </div>
              
              <div className="p-6 flex flex-col flex-grow">
                <h2 className="text-xl font-bold text-slate-900 mb-2">{course.title}</h2>
                <p className="text-slate-500 text-sm mb-6 line-clamp-3">{course.description}</p>
                
                <div className="mt-auto flex items-center justify-between">
                  <span className="text-indigo-600 font-bold text-lg">{course.price ? `${course.price} UZS` : 'Tekin'}</span>
                  <button className="bg-gradient-to-r from-violet-600 to-indigo-600 hover:from-violet-700 hover:to-indigo-700 text-white px-5 py-2.5 rounded-xl font-medium transition-all transform hover:-translate-y-0.5 shadow-md hover:shadow-indigo-500/30">Boshlash</button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}