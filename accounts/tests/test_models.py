from django.contrib.auth import get_user_model
from django.test import TestCase

from wordi.tests.mixins import TestFieldsParametersValuesMixin

User = get_user_model()


class UserTests(TestCase, TestFieldsParametersValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345',
        )
        cls.parameters_and_fields_with_value = {
            'verbose_name': {
                'email': 'адрес электронной почты',
                'first_name': 'имя',
                'last_name': 'фамилия',
                'date_joined': 'дата регистрации',
                'last_login': 'дата последнего входа',
                'is_staff': 'статус персонала',
                'is_admin': 'статус администратора',
                'is_superuser': 'статус суперпользователя',
                'is_email_verified': 'статус проверенной электронной почты',
                'last_password_update': 'дата последнего обновления пароля',
            },
            'default': {
                'is_staff': False,
                'is_admin': False,
                'is_superuser': False,
                'is_email_verified': False,
            },
            'max_length': {
                'email': 260,
                'first_name': 150,
                'last_name': 150,
            },
            'auto_now': {
                'last_login': True,
                'last_password_update': True,
            },
            'auto_now_add': {
                'date_joined': True,
            },
            'unique': {
                'email': True,
            }
        }

    def test_fields_parameters_values(self):
        super().run_fields_parameters_values_test(User)

    def test_model_username_field(self):
        self.assertEqual(User.USERNAME_FIELD, 'email')

    def test_model_required_fields(self):
        self.assertEqual(User.REQUIRED_FIELDS, ['first_name', 'last_name'])

    def test_str_method(self):
        self.assertEqual(str(self.user), str(self.user.email))

    def test_model_verbose_name(self):
        self.assertEqual(User._meta.verbose_name, 'пользователь')

    def test_model_verbose_name_plural(self):
        self.assertEqual(User._meta.verbose_name_plural, 'пользователи')

    def test_has_perm_method(self):
        self.assertEqual(self.user.has_perm(self, None), self.user.is_admin)

    def test_has_module_perms_method(self):
        self.assertTrue(self.user.has_module_perms(self))
