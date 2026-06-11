from django.db import models, transaction
from django.utils import timezone
from .models import Enrollment, LessonProgress
from .exceptions import AlreadyEnrolledError, CourseNotPublishedError
from courses.models import Course

class EnrollmentService:

    @staticmethod
    @transaction.atomic
    def enroll_user(user, course):
        # Ensure the course is actually published before enrolling
        if course.status != Course.Status.PUBLISHED:
            raise CourseNotPublishedError("Cannot enroll in an unpublished course.")

        # Prevent duplicate enrollments
        if Enrollment.objects.filter(student=user, course=course).exists():
            raise AlreadyEnrolledError("User is already enrolled in this course.")

        enrollment = Enrollment.objects.create(student=user, course=course)
        return enrollment

    @staticmethod
    @transaction.atomic
    def complete_course(enrollment):
        enrollment.is_completed = True
        enrollment.completed_at = timezone.now()
        enrollment.save(update_fields=['is_completed', 'completed_at'])
        return enrollment

    @staticmethod
    @transaction.atomic
    def update_progress(enrollment, lesson, watched_seconds):
        lesson_progress, _ = LessonProgress.objects.update_or_create(
            enrollment=enrollment,
            lesson=lesson,
            defaults={
                'watched_seconds': watched_seconds,
                'last_position': watched_seconds,
                'completed': watched_seconds > 0,
                'completed_at': timezone.now() if watched_seconds > 0 else None,
            }
        )

        total_lessons = enrollment.course.modules.aggregate(total=models.Count('lessons'))['total'] or 0
        completed_lessons = LessonProgress.objects.filter(enrollment=enrollment, completed=True).count()
        enrollment.progress_percent = min(100, int((completed_lessons / total_lessons) * 100)) if total_lessons else 0

        if enrollment.progress_percent >= 100:
            enrollment.is_completed = True
            enrollment.completed_at = timezone.now()

        enrollment.save(update_fields=['progress_percent', 'is_completed', 'completed_at'])
        return lesson_progress