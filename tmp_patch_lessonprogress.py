from pathlib import Path

path = Path('enrollments/models.py')
text = path.read_text(encoding='utf-8')
old = '''class LessonProgress(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="progresses"
    )

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="progresses"
    )

    is_completed = models.BooleanField(
        default=False
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.enrollment.user.username} - {self.lesson.title}"
'''
new = '''class LessonProgress(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="progresses"
    )

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="progresses"
    )

    watched_seconds = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    last_position = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.enrollment.student.username} - {self.lesson.title}"
'''
if old not in text:
    raise RuntimeError('Old block not found in enrollments/models.py')
text = text.replace(old, new)
path.write_text(text, encoding='utf-8')
print('updated enrollments/models.py')
