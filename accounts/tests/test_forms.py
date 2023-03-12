from django.test import TestCase

from accounts.forms import CustomUserCreationForm
from wordi.tests.mixins import TestFormFieldsLabels, TestFormFieldsMaxLength


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
