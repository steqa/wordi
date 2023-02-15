from django.test import TestCase

from accounts.models import User
from cards.models import Card
from wordi.tests.mixins import TestFieldsParametersValuesMixin


class CardTests(TestCase, TestFieldsParametersValuesMixin):
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
        cls.parameters_and_fields_with_value = {
            'verbose_name': {
                'user': 'пользователь',
                'front_text': 'текст на передней стороне',
                'back_text': 'текст на задней стороне',
                'date_created': 'дата создания',
                'date_updated': 'дата изменения',
            },
            'auto_now_add': {
                'date_created': True,
                'date_updated': True,
            }
        }

    def test_fields_parameters_values(self):
        super().run_fields_parameters_values_test(Card)

    def test_str_method(self):
        self.assertEqual(str(self.card), str(self.card.front_text[:25]))

    def test_model_verbose_name(self):
        self.assertEqual(Card._meta.verbose_name, 'карточка')

    def test_model_verbose_name_plural(self):
        self.assertEqual(Card._meta.verbose_name_plural, 'карточки')
