from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# --- Placeholder Ma'lumotlar (Real loyihada ma'lumotlar bazasidan olinadi) ---
class Course:
    def __init__(self, id, title, description, price):
        self.id = id
        self.title = title
        self.description = description
        self.price = price

class Enrollment:
    def __init__(self, course_id, course_title, progress_percent):
        # Course obyekti yaratiladi, chunki template enrollment.course.title ni chaqiradi
        self.course = Course(course_id, course_title, "", 0) 
        self.progress_percent = progress_percent
# --- Placeholder Ma'lumotlar Tugadi ---

def home_view(request):
    # Bosh sahifa (home.html) uchun eng so'nggi kurslar ro'yxatini yuboramiz
    courses = [
        Course(1, "Python dasturlash asoslari", "Python bilan dasturlash olamiga ilk qadam. O'zbek tilida sifatli darsliklar.", 350000),
        Course(2, "Web dasturlash (Django)", "Django frameworki yordamida zamonaviy veb ilovalar yarating.", 700000),
        Course(3, "Mobil dasturlash (Flutter)", "Flutter bilan cross-platform mobil ilovalar yaratishni o'rganing.", 900000),
    ]
    return render(request, 'home.html', {'courses': courses})

def course_list_view(request):
    courses = [
        Course(1, "Python dasturlash asoslari", "Python bilan dasturlash olamiga ilk qadam. O'zbek tilida sifatli darsliklar.", 350000),
        Course(2, "Web dasturlash (Django)", "Django frameworki yordamida zamonaviy veb ilovalar yarating.", 700000),
        Course(3, "Mobil dasturlash (Flutter)", "Flutter bilan cross-platform mobil ilovalar yaratishni o'rganing.", 900000),
        Course(4, "Ma'lumotlar bazalari (SQL)", "SQL tilini o'rganib, ma'lumotlar bilan samarali ishlashni o'zlashtiring.", None), # Narxi yo'q kurs uchun namuna
    ]
    return render(request, 'course_list.html', {'courses': courses})

@login_required(login_url='login')
def course_detail_view(request, pk):
    # Haqiqiy ilovada bu yerda Course.objects.get(pk=pk) bo'ladi
    course = Course(pk, f"Kurs {pk} sarlavhasi", f"Bu {pk}-sonli kursning batafsil tavsifi.", 400000)
    return render(request, 'course_detail.html', {'course': course})

@login_required(login_url='login')
def dashboard_view(request):
    enrollments = [
        Enrollment(1, "Python dasturlash asoslari", 75),
        Enrollment(2, "Web dasturlash (Django)", 30),
        Enrollment(3, "Mobil dasturlash (Flutter)", 0),
    ]
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
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role', 'student').strip()
        # Map legacy or unexpected role values to valid choices
        if role == 'teacher':
            role = 'instructor'
        allowed_roles = {'student', 'instructor', 'admin'}
        if role not in allowed_roles:
            role = 'student'

        User = get_user_model()
        if not username:
            username = email

        first_name = ''
        last_name = ''

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu login bilan ro‘yxatdan o‘tgan foydalanuvchi mavjud')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        if hasattr(user, 'role'):
            user.role = role
        user.save()

        # Auto-login after registration
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return redirect('login')

    return render(request, 'register.html')