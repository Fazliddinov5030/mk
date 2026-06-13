from django.db import models
from courses.models import Module

class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    points = models.IntegerField(default=1) # Har bir to'g'ri javob uchun ball

    class Meta:
        # Savollarni quiz ID si va ballar soniga ko'ra kompleks saralash uchun indeks
        indexes = [models.Index(fields=['quiz', 'points'])]

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False) # Faqat bitta yoxud bir nechta to'g'ri javob bo'lishi mumkin

    def __str__(self):
        return self.text