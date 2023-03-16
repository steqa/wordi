from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.forms import CustomPasswordResetForm, CustomUserCreationForm
from wordi.tests.mixins import TestFormFieldsLabels, TestFormFieldsMaxLength

User = get_user_model()


class CustomUserCreationFormTests(TestCase, TestFormFieldsLabels,
                                  TestFormFieldsMaxLength):
    @classmethod
    def setUpTestData(cls):
        cls.fields_with_labels = {
            'email': 'Адрес электронной почты',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }
        cls.fields_with_max_length = {
            'email': 260,
            'first_name': 150,
            'last_name': 150,
        }

    def test_form_fields_labels(self):
        form = CustomUserCreationForm()
        super().run_form_fields_labels_test(form)

    def test_form_fields_max_length(self):
        form = CustomUserCreationForm()
        super().run_form_fields_max_length_test(form)


class CustomPasswordResetFormTests(TestCase, TestFormFieldsLabels,
                                   TestFormFieldsMaxLength):
    @classmethod
    def setUpTestData(cls):
        cls.fields_with_labels = {
            'email': 'Адрес электронной почты',
        }
        cls.fields_with_max_length = {
            'email': 260,
        }

    def test_form_fields_labels(self):
        form = CustomPasswordResetForm()
        super().run_form_fields_labels_test(form)

    def test_form_fields_max_length(self):
        form = CustomPasswordResetForm()
        super().run_form_fields_max_length_test(form)
