from django.contrib import admin

from .models import LessonStats


@admin.register(LessonStats)
class LessonStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'correct_answers', 'consecutive_days')
    search_fields = ('user', 'date', 'correct_answers', 'consecutive_days')
    list_filter = ('user', 'date', 'correct_answers', 'consecutive_days')
    readonly_fields = ('id', 'date',)
    fieldsets = (
        (None,
            {'fields': (
                'id',
                'user',
            )}),
        ('Статистика',
            {'fields': (
                'date',
                'correct_answers',
                'consecutive_days'
            )}),
    )
