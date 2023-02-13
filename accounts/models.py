from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="адрес электронной почты", max_length=260, unique=True)
    first_name = models.CharField(
        verbose_name="имя", max_length=150)
    last_name = models.CharField(
        verbose_name="фамилия", max_length=150)
    date_joined = models.DateTimeField(
        verbose_name="дата регистрации", auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name="дата последнего входа", auto_now=True)
    is_staff = models.BooleanField(
        verbose_name="статус персонала", default=False)
    is_admin = models.BooleanField(
        verbose_name="статус администратора", default=False)
    is_superuser = models.BooleanField(
        verbose_name="статус суперпользователя", default=False)
    is_email_verified = models.BooleanField(
        verbose_name="статус проверенной электронной почты", default=False)
    last_password_update = models.DateTimeField(
        verbose_name="дата последнего обновления пароля", auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
