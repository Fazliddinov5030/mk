from django.db import models
from django.conf import settings
from courses.models import Course, Lesson


class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )

    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress_percent = models.PositiveIntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("student", "course")
        ordering = ["-enrolled_at"]

    def __str__(self):
        return f"{self.student.username} → {self.course.title}"


class LessonProgress(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="progresses",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="progresses",
    )

    watched_seconds = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    last_position = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ("enrollment", "lesson")

    def __str__(self):
        return f"{self.enrollment.student.username} - {self.lesson.title}"