from rest_framework import serializers
from .models import Enrollment, LessonProgress

class LessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = ('id', 'lesson', 'watched_seconds', 'completed', 'last_position')
        read_only_fields = ('completed',)

class EnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    student_name = serializers.CharField(source='student.username', read_only=True)

    class Meta:
        model = Enrollment
        fields = (
            'id', 'course', 'course_title',
            'student_name', 'enrolled_at',
            'progress_percent', 'completed_at'
        )
        read_only_fields = ('student', 'enrolled_at', 'progress_percent', 'completed_at')

class EnrollSerializer(serializers.Serializer):
    """Kursga yozilish uchun"""
    course_id = serializers.IntegerField()