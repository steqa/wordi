from datetime import date, timedelta

from django.db.models.query import QuerySet

from .models import LessonStats


def get_last_consecutive_days(lesson_stats: QuerySet[LessonStats]) -> int:
    if lesson_stats.exists():
        lesson_stats = lesson_stats.first()
        today = date.today()
        yesterday = date.today() - timedelta(days=1)
        if (lesson_stats.date == today) or (lesson_stats.date == yesterday):
            last_consecutive_days = lesson_stats.consecutive_days + 1
        else:
            last_consecutive_days = 0
    else:
        last_consecutive_days = 0

    return last_consecutive_days


def get_today_lesson_complete(lesson_stats: QuerySet[LessonStats]) -> bool:
    today_lesson_complete = False
    if lesson_stats.exists():
        lesson_stats = lesson_stats.first()
        if lesson_stats.date == date.today():
            today_lesson_complete = True

    return today_lesson_complete
