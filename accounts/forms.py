from django import forms
from django.contrib.auth.forms import (PasswordResetForm, SetPasswordForm,
                                       UserCreationForm)

from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Адрес электронной почты',
        max_length=260)
    first_name = forms.CharField(
        label='Имя',
        max_length=150)
    last_name = forms.CharField(
        label='Фамилия',
        max_length=150)
    password1 = forms.CharField(
        label='Пароль')
    password2 = forms.CharField(
        label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        field_classes = {}


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Адрес электронной почты',
        max_length=260)
