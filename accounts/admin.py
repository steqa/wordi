from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'date_joined', 'is_email_verified')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('id', 'date_joined', 'last_login',
                       'last_password_update')
    fieldsets = (
        (None,
            {'fields': (
                readonly_fields[0],
                'email',
                'password'
            )}),
        ('Персональная информация',
            {'fields': (
                'first_name',
                'last_name',
            )}),
        ('Права доступа',
            {'fields': (
                'is_staff',
                'is_admin',
                'is_superuser',
                'is_email_verified',
            )}),
        ('Важные даты',
            {'fields': (
                readonly_fields[1],
                readonly_fields[2],
                readonly_fields[3],
            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    ordering = ()
    filter_horizontal = ()
    list_filter = ()
