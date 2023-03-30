from django.db import models

from accounts.models import User


class LessonStats(models.Model):
    user = models.ForeignKey(
        User, verbose_name="пользователь", on_delete=models.CASCADE)
    date = models.DateField(
        verbose_name="дата", auto_now_add=True)
    correct_answers = models.PositiveIntegerField(
        verbose_name="количество правильных ответов", default=0)
    consecutive_days = models.PositiveIntegerField(
        verbose_name="количество последовательных дней", default=0)

    class Meta:
        verbose_name = 'статистика пользователя'
        verbose_name_plural = 'статистика пользователей'
        unique_together = ('user', 'date')

    def __str__(self):
        return f'{self.user} - {self.date}'
