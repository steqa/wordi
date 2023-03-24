import os

from accounts.models import User
from wordi import settings

from .data_classes import CardData, CardImagesData
from .models import Card, CardImages


def create_card(
        user: User, card_data: CardData) -> Card:
    card = Card(
        user=user,
        front_text=card_data.front_text,
        back_text=card_data.back_text
    )
    card.save()
    return card


def create_card_images(
        card: Card, card_images_data: CardImagesData) -> CardImages:
    card_images = CardImages(
        card=card,
        front_image=card_images_data.front_image[0],
        back_image=card_images_data.back_image[0]
    )
    card_images.save()
    return card_images


def delete_card_images_directory(user: User, card_pk: int) -> None:
    dir_path = os.path.join(
        settings.MEDIA_ROOT, 'user_images',
        str(user.pk), str(card_pk))
    if os.path.exists(dir_path):
        os.rmdir(dir_path)
