from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from accounts.services import UserService
from accounts.exceptions import UserAlreadyExistsError

from courses.models import Course
from enrollments.models import Enrollment

def home_view(request):
    # N+1 muammosini oldini olish: kursga tegishli o'qituvchi va modullar oldindan yuklanadi
    courses = Course.objects.select_related('instructor').prefetch_related('modules')[:3]
    return render(request, 'home.html', {'courses': courses})

def course_list_view(request):
    courses = Course.objects.select_related('instructor').prefetch_related('modules').all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required(login_url='login')
def course_detail_view(request, pk):
    course = Course.objects.select_related(
        'instructor'
    ).prefetch_related(
        'modules__lessons' # Modullar va uning ichidagi darslarni birdan yuklash
    ).get(pk=pk)
    return render(request, 'course_detail.html', {'course': course})

@login_required(login_url='login')
def dashboard_view(request):
    # Talabaning kurslari (kursdagi o'qituvchi va foydalanuvchi dars progressi bilan birga)
    enrollments = Enrollment.objects.filter(student=request.user).select_related(
        'course__instructor'
    ).prefetch_related(
        'progresses' 
    )
    return render(request, 'dashboard.html', {'enrollments': enrollments})

def chat_view(request):
    return render(request, 'chat.html')

@login_required(login_url='login')
def profile_view(request):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Login yoki parol noto‘g‘ri')
        return render(request, 'login.html')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        role = request.POST.get('role', 'student').strip()

        if not username or not email or not password:
            messages.error(request, 'Iltimos, barcha maydonlarni to‘ldiring.')
            return render(request, 'register.html')

        if len(password) < 8:
            messages.error(request, 'Parol kamida 8 ta belgidan iborat bo‘lishi kerak.')
            return render(request, 'register.html')

        try:
            UserService.register_user(username, email, password, role)
        except UserAlreadyExistsError as e:
            messages.error(request, str(e))
            return render(request, 'register.html')

        # Auto-login after registration
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return redirect('login')

    return render(request, 'register.html')