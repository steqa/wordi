from datetime import date, timedelta

from django.test import TestCase

from accounts.models import User
from stats.models import LessonStats
from stats.utils import (get_correct_answers_by_day, get_last_consecutive_days,
                         get_today_lesson_complete, validate_year)


class UtilsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345'
        )

    def test_get_last_consecutive_days(self):
        with self.subTest('test 1'):
            lesson_stats = LessonStats.objects.filter(
                user=self.user).order_by('-id')[:1]
            real_value = get_last_consecutive_days(lesson_stats)
            self.assertEqual(real_value, 0)

        with self.subTest('test 2'):
            LessonStats.objects.create(
                user=self.user,
            )
            lesson_stats = LessonStats.objects.filter(
                user=self.user).order_by('-id')[:1]
            real_value = get_last_consecutive_days(lesson_stats)
            self.assertEqual(real_value, 1)

        with self.subTest('test 3'):
            LessonStats.objects.create(
                user=self.user,
                date=date.today() - timedelta(days=1),
                consecutive_days=1
            )
            lesson_stats = LessonStats.objects.filter(
                user=self.user).order_by('-id')[:1]
            real_value = get_last_consecutive_days(lesson_stats)
            self.assertEqual(real_value, 2)

    def test_get_today_lesson_complete(self):
        with self.subTest('test 1'):
            lesson_stats = LessonStats.objects.filter(
                user=self.user).order_by('-id')[:1]
            real_value = get_today_lesson_complete(lesson_stats)
            self.assertEqual(real_value, False)

        with self.subTest('test 2'):
            LessonStats.objects.create(
                user=self.user,
                date=date.today() - timedelta(days=1),
            )
            lesson_stats = LessonStats.objects.filter(
                user=self.user).order_by('-id')[:1]
            real_value = get_today_lesson_complete(lesson_stats)
            self.assertEqual(real_value, False)

        with self.subTest('test 3'):
            LessonStats.objects.create(
                user=self.user,
            )
            lesson_stats = LessonStats.objects.filter(
                user=self.user).order_by('-id')[:1]
            real_value = get_today_lesson_complete(lesson_stats)
            self.assertEqual(real_value, True)

    def test_validate_year(self):
        YEARS_WITH_VALIDATION_STATUS = {
            '': False,
            'test': False,
            '0': False,
            str((date.today() + timedelta(days=1)).year): False,
            str(date.today().year): True,
        }
        for year, expected_value in YEARS_WITH_VALIDATION_STATUS.items():
            with self.subTest(f'{year=}, {expected_value=}'):
                real_value = validate_year(year)
                self.assertEqual(real_value, expected_value)

    def test_get_correct_answers_by_day(self):
        with self.subTest('test 1'):
            lesson_stats = LessonStats.objects.filter(user=self.user)
            real_value = get_correct_answers_by_day(lesson_stats)
            expected_value = {}
            self.assertEqual(real_value, expected_value)

        with self.subTest('test 2'):
            LessonStats.objects.create(
                user=self.user,
                correct_answers=3
            )
            lesson_stats = LessonStats.objects.filter(user=self.user)
            real_value = get_correct_answers_by_day(lesson_stats)
            expected_value = {f'{date.today()}': 3}
            self.assertEqual(real_value, expected_value)
