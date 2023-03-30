from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from stats.models import LessonStats
from wordi.tests.mixins import TestFieldsParametersValuesMixin

User = get_user_model()


class LessonStatsTests(TestCase, TestFieldsParametersValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345',
        )
        cls.LessonStats = LessonStats.objects.create(
            user=cls.user,
        )
        cls.parameters_and_fields_with_value = {
            'verbose_name': {
                'user': 'пользователь',
                'date': 'дата',
                'correct_answers': 'количество правильных ответов',
                'consecutive_days': 'количество последовательных дней'
            },
            'default': {
                'date': date.today,
                'correct_answers': 0,
                'consecutive_days': 0
            }
        }

    def test_fields_parameters_values(self):
        super().run_fields_parameters_values_test(LessonStats)

    def test_str_method(self):
        self.assertEqual(
            LessonStats.__str__(self.LessonStats),
            f'test@gmail.com - {date.today()}'
        )

    def test_model_verbose_name(self):
        self.assertEqual(LessonStats._meta.verbose_name,
                         'статистика пользователя')

    def test_model_verbose_name_plural(self):
        self.assertEqual(LessonStats._meta.verbose_name_plural,
                         'статистика пользователей')

    def test_model_unique_together(self):
        self.assertEqual(LessonStats._meta.unique_together,
                         (('user', 'date'),))
