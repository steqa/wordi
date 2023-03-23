from django.db import models
from django_cleanup import cleanup

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


def _get_card_front_image_filepath(self, image_name: str) -> str:
    return f'user_images/{self.card.user.pk}/{self.card.id}/front_image.jpg'


def _get_card_back_image_filepath(self, image_name: str) -> str:
    return f'user_images/{self.card.user.pk}/{self.card.id}/back_image.jpg'


@cleanup.select
class CardImages(models.Model):
    card = models.ForeignKey(
        Card, verbose_name='карточка', on_delete=models.CASCADE)
    front_image = models.ImageField(
        verbose_name="изображение на передней стороне",
        upload_to=_get_card_front_image_filepath, blank=True, null=True)
    back_image = models.ImageField(
        verbose_name="изображение на задней стороне",
        upload_to=_get_card_back_image_filepath, blank=True, null=True)

    class Meta:
        verbose_name = 'изображения карточки'
        verbose_name_plural = 'изображения карточек'

    def __str__(self):
        return str(self.card)
