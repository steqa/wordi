import os

from django.core.files.uploadedfile import TemporaryUploadedFile
from django.test import TestCase
from pydantic import ValidationError

from accounts.models import User
from cards.models import Card
from cards.utils import (create_and_get_card_images_without_save,
                         create_and_get_card_without_save,
                         delete_card_images_directory)


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
        JSON_AND_EXPECTED_CARD_PARAMETERS = {
            '{}':
                ValidationError,
            '{"formFrontText": "", "formBackText": "Back Text"}':
                ValidationError,
            '{"formFrontText": "Front Text", "formBackText": "Back Text"}':
                {'card': self.card,
                 'front_text': 'Front Text',
                 'back_text': 'Back Text'},
        }
        for json, expected_card_parameters in \
                JSON_AND_EXPECTED_CARD_PARAMETERS.items():
            with self.subTest(f'{json=}'):
                try:
                    card = create_and_get_card_without_save(
                        user=self.user, json=json)
                    real_card_parameters = {'card': self.card,
                                            'front_text': card.front_text,
                                            'back_text': card.back_text}
                except ValidationError:
                    real_card_parameters = ValidationError

                self.assertEqual(real_card_parameters,
                                 expected_card_parameters)

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

    def test_delete_card_images_directory(self):
        with self.subTest('test: 1'):
            dir_path = '/home/steqa/wordi/static/images/user_images/1/0'
            os.mkdir(dir_path)
            try:
                delete_card_images_directory(user=self.user, card_pk=0)
                os.path.exists(dir_path)
            except:
                dir_exists = True
                os.rmdir(dir_path)
            else:
                dir_exists = False
            self.assertFalse(dir_exists)
