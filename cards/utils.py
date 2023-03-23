import os

from pydantic import ValidationError

from accounts.models import User
from wordi import settings

from .data_classes import CardData, CardImagesData
from .models import Card, CardImages


def create_and_get_card_without_save(user: User, json: str) -> Card:
    try:
        card_data = CardData.parse_raw(json)
    except ValidationError as e:
        raise e
    else:
        card = Card(
            user=user,
            front_text=card_data.front_text,
            back_text=card_data.back_text
        )
        return card


def create_and_get_card_images_without_save(
        card: Card, images_dict: dict) -> CardImages | None:
    try:
        card_images_data = CardImagesData.parse_obj(images_dict)
    except ValidationError as e:
        raise e
    else:
        front_image = card_images_data.front_image[0] if \
            card_images_data.front_image is not None else \
            card_images_data.front_image
        back_image = card_images_data.back_image[0] if \
            card_images_data.back_image is not None else \
            card_images_data.back_image
        if (front_image is not None) or (back_image is not None):
            card_images = CardImages(
                card=card,
                front_image=front_image,
                back_image=back_image
            )
            return card_images


def delete_card_images_directory(user: User, card_pk: int) -> None:
    dir_path = os.path.join(
        settings.MEDIA_ROOT, 'user_images',
        str(user.pk), str(card_pk))
    os.rmdir(dir_path)
