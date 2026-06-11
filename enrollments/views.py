from django.shortcuts import render
import logging
from rest_framework import generics, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from courses.models import Course
from .models import Enrollment
from .serializers import EnrollmentSerializer, EnrollSerializer, LessonProgressSerializer
from .services import EnrollmentService
from .exceptions import AlreadyEnrolledError, CourseNotPublishedError
from courses.permissions import IsStudent

logger = logging.getLogger(__name__)

class EnrollmentViewSet(GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, IsStudent)

    def get_queryset(self):
        return Enrollment.objects.filter(
            student=self.request.user
        ).select_related('course', 'student')

    @action(detail=False, methods=['post'])
    def enroll(self, request):
        """Kursga yozilish"""
        serializer = EnrollSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            course = Course.objects.get(id=serializer.validated_data['course_id'])
            enrollment = EnrollmentService.enroll_user(request.user, course)
            return Response(
                EnrollmentSerializer(enrollment).data,
                status=status.HTTP_201_CREATED
            )
        except Course.DoesNotExist:
            return Response({'error': 'Kurs topilmadi'}, status=404)
        except AlreadyEnrolledError:
            return Response({'error': 'Siz allaqachon bu kursga yozilgansiz'}, status=400)
        except CourseNotPublishedError:
            return Response({'error': 'Kurs hali nashr qilinmagan'}, status=400)

    @action(detail=False, methods=['get'])
    def my_courses(self, request):
        """Mening kurslarim"""
        enrollments = self.get_queryset()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def progress(self, request, pk=None):
        """Dars progressini saqlash"""
        enrollment = self.get_queryset().get(pk=pk)
        serializer = LessonProgressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        EnrollmentService.update_progress(
            enrollment=enrollment,
            lesson=serializer.validated_data['lesson'],
            watched_seconds=serializer.validated_data['watched_seconds']
        )
        return Response({'message': 'Progress saqlandi'})
