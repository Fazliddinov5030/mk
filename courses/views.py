from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from .models import Course, Category, Module, Lesson
from .serializers import CourseSerializer, CategorySerializer, ModuleSerializer, LessonSerializer
from enrollments.serializers import EnrollmentSerializer # Yoki CourseSerializer
from book.services import SearchEngine

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # View-level cache: Sahifani 15 daqiqaga keshlaydi
    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('q', None)
        if search_query:
            queryset = SearchEngine.full_text_search(search_query)
        return queryset

class CourseStatsView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # Low-level cache: Agar keshda bo'lsa darhol qaytaradi, bo'lmasa DB'dan hisoblab keshga saqlaydi
        cache_key = 'global_course_stats'
        stats = cache.get(cache_key)
        
        if not stats:
            stats = {"total_courses": Course.objects.count()} # DB operatsiyasi
            cache.set(cache_key, stats, timeout=60*60) # 1 soatga saqlash
            
        return Response(stats)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.delete('global_course_stats') # Cache invalidation

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.delete('global_course_stats') # Cache invalidation


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if 'course_pk' in self.kwargs:
            return self.queryset.filter(course_id=self.kwargs['course_pk'])
        return super().get_queryset()


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if 'module_pk' in self.kwargs:
            return self.queryset.filter(module_id=self.kwargs['module_pk'])
        return super().get_queryset()