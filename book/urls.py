"""
URL configuration for book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

import main_views

urlpatterns = [
    # Frontend URL'lari
    path('', main_views.home_view, name='home'),
    path('search/', main_views.course_list_view, name='course_search'),
    path('courses/', main_views.course_list_view, name='course_list'),
    path('courses/<int:pk>/', main_views.course_detail_view, name='course_detail'),
    path('dashboard/', main_views.dashboard_view, name='dashboard'),
    path('profile/', main_views.profile_view, name='profile'),
    path('chat/', main_views.chat_view, name='chat'),
    path('login/', main_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', main_views.register_view, name='register'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/enrollments/', include('enrollments.urls')),
    path('api/', include('courses.urls')),
    path('api/certificates/', include('certificates.urls')),

]
