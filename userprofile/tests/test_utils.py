from django.test import TestCase

from accounts.data_classes import UserChangeData, UserChangePasswordData
from accounts.models import User
from userprofile.utils import (edit_user, get_personal_data_errors,
                               password_data_is_not_empty)


class UtilsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345'
        )

    def test_get_personal_data_errors(self):
        JSON_AND_EXPECTED_ERRORS = {
            '{}': {},
            '{"formEmail": "test@test.test"}': {},
            '{"formEmail": ""}': {'email': ['Обязательное поле.']}
        }
        for json, expected_errors in JSON_AND_EXPECTED_ERRORS.items():
            with self.subTest(f'{json=}, {expected_errors=}'):
                data = UserChangeData.parse_raw(json)
                real_errors = get_personal_data_errors(data)
                self.assertEqual(real_errors, expected_errors)

    def test_edit_user(self):
        JSON_AND_EXPECTED_USER_PARAMETERS = {
            '{}': {'email': 'test@gmail.com',
                   'first_name': 'Имя',
                   'last_name': 'Фамилия'},
            '{"formEmail": ""}': {'email': '',
                                  'first_name': 'Имя',
                                  'last_name': 'Фамилия'},
            '{"formFirstName": "Новое имя"}': {'email': '',
                                               'first_name': 'Новое имя',
                                               'last_name': 'Фамилия'}
        }
        for json, expected_user_parameters in \
                JSON_AND_EXPECTED_USER_PARAMETERS.items():
            with self.subTest(f'{json=}, {expected_user_parameters=}'):
                data = UserChangeData.parse_raw(json)
                user = edit_user(self.user, data)
                real_user_parameters = {'email': user.email,
                                        'first_name': user.first_name,
                                        'last_name': user.last_name}
                self.assertEqual(real_user_parameters,
                                 expected_user_parameters)

    def test_password_data_is_not_empty(self):
        JSON_AND_PASSWORD_DATA_IS_NOT_EMPTY = {
            '{}': False,
            '{"formOldPassword": ""}': True,
            '{"formNewPassword1": "new password"}': True
        }
        for json, expected_password_data_is_not_empty in \
                JSON_AND_PASSWORD_DATA_IS_NOT_EMPTY.items():
            with self.subTest(
                    f'{json=}, {expected_password_data_is_not_empty=}'):
                data = UserChangePasswordData.parse_raw(json)
                real_password_data_is_not_empty = \
                    password_data_is_not_empty(data)
                self.assertEqual(real_password_data_is_not_empty,
                                 expected_password_data_is_not_empty)
