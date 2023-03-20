from django.test import TestCase

from accounts.forms import (CustomPasswordChangeForm, CustomPasswordResetForm,
                            CustomSetPasswordForm, CustomUserChangeForm,
                            CustomUserCreationForm)
from accounts.models import User
from wordi.tests.mixins import TestFormFieldsLabels, TestFormFieldsMaxLength


class CustomUserCreationFormTests(
        TestCase, TestFormFieldsLabels,
        TestFormFieldsMaxLength):
    @classmethod
    def setUpTestData(cls):
        cls.fields_with_labels = {
            'email': 'Адрес электронной почты',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля'
        }
        cls.fields_with_max_length = {
            'email': 260,
            'first_name': 150,
            'last_name': 150
        }

    def test_form_fields_labels(self):
        form = CustomUserCreationForm()
        super().run_form_fields_labels_test(form)

    def test_form_fields_max_length(self):
        form = CustomUserCreationForm()
        super().run_form_fields_max_length_test(form)


class CustomPasswordResetFormTests(
        TestCase, TestFormFieldsLabels,
        TestFormFieldsMaxLength):
    @classmethod
    def setUpTestData(cls):
        cls.fields_with_labels = {
            'email': 'Адрес электронной почты'
        }
        cls.fields_with_max_length = {
            'email': 260
        }

    def test_form_fields_labels(self):
        form = CustomPasswordResetForm()
        super().run_form_fields_labels_test(form)

    def test_form_fields_max_length(self):
        form = CustomPasswordResetForm()
        super().run_form_fields_max_length_test(form)


class CustomSetPasswordFormTests(
        TestCase, TestFormFieldsLabels,
        TestFormFieldsMaxLength):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345'
        )
        cls.fields_with_labels = {
            'new_password1': 'Новый пароль',
            'new_password2': 'Подтверждение нового пароля'
        }

    def test_form_fields_labels(self):
        form = CustomSetPasswordForm(self.user)
        super().run_form_fields_labels_test(form)


class CustomUserChangeFormTests(
        TestCase, TestFormFieldsLabels,
        TestFormFieldsMaxLength):
    @classmethod
    def setUpTestData(cls):
        cls.fields_with_labels = {
            'email': 'Адрес электронной почты',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        cls.fields_with_max_length = {
            'email': 260,
            'first_name': 150,
            'last_name': 150
        }

    def test_form_fields_labels(self):
        form = CustomUserChangeForm()
        super().run_form_fields_labels_test(form)

    def test_form_fields_max_length(self):
        form = CustomUserChangeForm()
        super().run_form_fields_max_length_test(form)


class CustomPasswordChangeFormTests(
        TestCase, TestFormFieldsLabels,
        TestFormFieldsMaxLength):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345'
        )
        cls.fields_with_labels = {
            'old_password': 'Старый пароль',
            'new_password1': 'Новый пароль',
            'new_password2': 'Подтверждение нового пароля'
        }

    def test_form_fields_labels(self):
        form = CustomPasswordChangeForm(self.user)
        super().run_form_fields_labels_test(form)
