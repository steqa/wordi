import os

from django.test import TestCase

from accounts.models import User
from cards.models import Card
from cards.utils import delete_card_images_directory


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
