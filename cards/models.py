from django.db import models

from accounts.models import User


class Card(models.Model):
    user = models.ForeignKey(
        User, verbose_name="пользователь", on_delete=models.CASCADE)
    front_text = models.TextField(
        verbose_name="текст на передней стороне")
    back_text = models.TextField(
        verbose_name="текст на задней стороне")
    date_created = models.DateTimeField(
        verbose_name="дата создания", auto_now_add=True)
    date_updated = models.DateTimeField(
        verbose_name="дата изменения", auto_now_add=True)

    class Meta:
        verbose_name = 'карточка'
        verbose_name_plural = 'карточки'

    def __str__(self):
        return self.front_text[:25]
