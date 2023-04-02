from datetime import date, timedelta

from django.db.models.query import QuerySet

from accounts.models import User

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


def validate_year(year: str) -> bool:
    if year.isnumeric():
        year = int(year)
        if (year <= date.today().year) and (year > 0):
            return True
        else:
            return False
    else:
        return False


def get_calendar_data_for_year(user: User, year: int) -> dict:
    date_start = date(year, 1, 1)
    date_end = date(year, 12, 31)

    lessons_stats = LessonStats.objects.filter(
        user=user,
        date__gte=date_start,
        date__lte=date_end
    )

    correct_answers_by_day = get_correct_answers_by_day(lessons_stats)
    return correct_answers_by_day


def get_correct_answers_by_day(lessons_stats: QuerySet[LessonStats]) -> dict:
    correct_answers_by_day = {}
    for lesson_stats in lessons_stats:
        date_str = lesson_stats.date.strftime('%Y-%m-%d')
        correct_answers_by_day[date_str] = lesson_stats.correct_answers

    return correct_answers_by_day


def get_consecutive_days(user: User) -> int:
    yesterday = date.today() - timedelta(days=1)

    last_lesson_stats = LessonStats.objects.filter(
        user=user).order_by('-date').first()

    if (last_lesson_stats) and (last_lesson_stats.date == yesterday):
        consecutive_days = last_lesson_stats.consecutive_days + 1
    else:
        consecutive_days = 0

    return consecutive_days


def save_stats(
        user: User, correct_answers: int,
        consecutive_days: int) -> LessonStats:
    lesson_stats, created = LessonStats.objects.get_or_create(
        user=user,
        date=date.today()
    )
    if created:
        lesson_stats.consecutive_days = consecutive_days
    lesson_stats.correct_answers += correct_answers
    lesson_stats.save()
    return lesson_stats
