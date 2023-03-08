from django.core.files.uploadedfile import TemporaryUploadedFile
from django.test import TestCase

from accounts.models import User
from cards.models import Card
from cards.utils import (create_and_get_card_images_without_save,
                         create_and_get_card_without_save)


class UtilsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345',
        )
        cls.card = Card.objects.create(
            user=cls.user,
            front_text='тестовый текст на передней стороне',
            back_text='тестовый текст на задней стороне',
        )

    def test_create_and_get_card_without_save(self):
        json = '{"formFrontText": "Front Text", "formBackText": "Back Text"}'
        card = create_and_get_card_without_save(
            user=self.user, json=json)
        self.assertEqual(card.user, self.user)
        self.assertEqual(card.front_text, 'Front Text')
        self.assertEqual(card.back_text, 'Back Text')

    def test_create_and_get_card_images_without_save(self):
        with self.subTest('test: 1'):
            images_dict = {}
            card_images = create_and_get_card_images_without_save(
                card=self.card, images_dict=images_dict)
            self.assertEqual(card_images, None)

        with self.subTest('test: 2'):
            front_image = TemporaryUploadedFile(
                'front_image', 'image/jpeg', 1, None)
            back_image = TemporaryUploadedFile(
                'back_image', 'image/jpeg', 0, None)
            images_dict = {
                'formFrontImage': [front_image],
                'formBackImage': [back_image]
            }
            card_images = create_and_get_card_images_without_save(
                card=self.card, images_dict=images_dict)
            self.assertEqual(card_images.card, self.card)
            self.assertEqual(card_images.front_image, front_image)
            self.assertEqual(card_images.back_image, back_image)
