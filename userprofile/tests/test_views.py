from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from wordi.tests.mixins import TestPagesUsesCorrectTemplateMixin

User = get_user_model()


class UserprofilePagesTests(
        TestCase, TestPagesUsesCorrectTemplateMixin):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345'
        )
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)
        cls.templates_pages_names = {
            'userprofile/edit-userprofile.html': reverse('edit-userprofile'),
        }

    def test_pages_uses_correct_template(self):
        super().run_pages_uses_correct_template_test()
