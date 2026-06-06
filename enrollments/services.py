import logging
from django.db import transaction
from courses.models import Course
from accounts.models import User
from .models import Enrollment, LessonProgress
from .exceptions import AlreadyEnrolledError, CourseNotPublishedError

logger = logging.getLogger(__name__)

class EnrollmentService:

    @staticmethod
    @transaction.atomic
    def enroll(user: User, course: Course) -> Enrollment:
        """Talabani kursga yozish"""

        # 1. Kurs nashr qilinganmi?
        if course.status != 'published':
            raise CourseNotPublishedError()

        # 2. Allaqachon yozilganmi?
        if Enrollment.objects.filter(student=user, course=course).exists():
            raise AlreadyEnrolledError()

        # 3. Yozish
        enrollment = Enrollment.objects.create(
            student=user,
            course=course,
            progress_percent=0
        )

        logger.info(
            'Talaba kursga yozildi',
            extra={'user_id': user.id, 'course_id': course.id}
        )

        return enrollment

    @staticmethod
    @transaction.atomic
    def update_progress(enrollment: Enrollment, lesson_id: int, watched_seconds: int) -> None:
        """Dars progressini yangilash"""

        # 1. LessonProgress yangilash
        progress, _ = LessonProgress.objects.get_or_create(
            enrollment=enrollment,
            lesson_id=lesson_id
        )
        progress.watched_seconds = watched_seconds

        # 2. 90% dan ko'p ko'rsa — tugatilgan deb hisoblash
        if watched_seconds >= progress.lesson.duration_seconds * 0.9:
            progress.completed = True

        progress.last_position = watched_seconds
        progress.save()

        # 3. Umumiy progress hisoblash
        EnrollmentService._recalculate_progress(enrollment)

    @staticmethod
    def _recalculate_progress(enrollment: Enrollment) -> None:
        """Kurs progressini foizda hisoblash"""
        from courses.models import Lesson

        total = Lesson.objects.filter(
            module__course=enrollment.course
        ).count()

        if total == 0:
            return

        completed = LessonProgress.objects.filter(
            enrollment=enrollment,
            completed=True
        ).count()

        enrollment.progress_percent = (completed / total) * 100
        enrollment.save()

        # 4. 100% bo'lsa — kurs tugadi
        if enrollment.progress_percent == 100:
            from django.utils import timezone
            enrollment.completed_at = timezone.now()
            enrollment.save()