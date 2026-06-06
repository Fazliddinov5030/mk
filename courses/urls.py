from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedSimpleRouter
from .views import CourseViewSet, ModuleViewSet, LessonViewSet, CategoryViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')
router.register('categories', CategoryViewSet, basename='category')

# Nested routers for hierarchical URL patterns (courses -> modules -> lessons)
courses_router = NestedSimpleRouter(router, 'courses', lookup='course')
courses_router.register('modules', ModuleViewSet, basename='course-modules')

modules_router = NestedSimpleRouter(courses_router, 'modules', lookup='module')
modules_router.register('lessons', LessonViewSet, basename='module-lessons')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(courses_router.urls)),
    path('', include(modules_router.urls)),
]