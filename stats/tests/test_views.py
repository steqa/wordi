from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from stats.models import LessonStats
from stats.utils import get_last_consecutive_days, get_today_lesson_complete
from wordi.tests.mixins import (TestPagesShowCorrectContextMixin,
                                TestPagesUsesCorrectTemplateMixin)

User = get_user_model()


class CardsPagesTests(TestCase, TestPagesUsesCorrectTemplateMixin,
                      TestPagesShowCorrectContextMixin):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345',
        )
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)
        cls.templates_pages_names = {
            'stats/stats.html': reverse('stats'),
        }
        LessonStats.objects.create(
            user=cls.user
        )
        cls.lessons_stats = LessonStats.objects.filter(
            user=cls.user).order_by('-id')[:1]

    def test_pages_uses_correct_template(self):
        super().run_pages_uses_correct_template_test()

    def test_pages_show_correct_context(self):
        with self.subTest('test 1'):
            response = self.authorized_client.get(reverse('stats'))
            expected_context_value = get_last_consecutive_days(
                self.lessons_stats)
            real_context_value = response.context['last_consecutive_days']
            self.assertEqual(real_context_value, expected_context_value)

        with self.subTest('test 2'):
            response = self.authorized_client.get(reverse('stats'))
            expected_context_value = get_today_lesson_complete(
                self.lessons_stats)
            real_context_value = response.context['today_lesson_complete']
            self.assertEqual(real_context_value, expected_context_value)
