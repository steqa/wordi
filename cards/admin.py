from django.contrib import admin

from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'front_text', 'back_text')
    search_fields = ('user', 'front_text', 'back_text')
    list_filter = ('date_created', 'date_updated')
    readonly_fields = ('id', 'date_created', 'date_updated')
    fieldsets = (
        (None,
            {'fields': (
                'id',
                'user',
            )}),
        ('Передняя сторона',
            {'fields': (
                'front_text',
            )}),
        ('Задняя сторона',
            {'fields': (
                'back_text',
            )}),
        ('Важные даты',
            {'fields': (
                'date_created',
                'date_updated',
            )}),
    )
