from django.db import transaction
from django.utils import timezone
from .models import Enrollment
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
        enrollment.save(update_fields=['is_completed'])
        return enrollment