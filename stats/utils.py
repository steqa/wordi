from datetime import date, timedelta
from typing import NamedTuple

from django.db.models.query import QuerySet

from accounts.models import User

from .models import LessonStats


class Period(NamedTuple):
    date_start: date
    date_end: date


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


def get_calendar_data_for_year(user: User, year: int) -> list[tuple]:
    date_start = date(year, 1, 1)
    date_end = date(year, 12, 31)
    period = Period(date_start=date_start, date_end=date_end)

    lessons_stats = LessonStats.objects.filter(
        user=user,
        date__gte=period.date_start,
        date__lte=period.date_end
    )

    correct_answers_by_day = get_correct_answers_by_day(lessons_stats)
    calendar_data = get_calendar_data_for_period(
        correct_answers_by_day, period)
    return calendar_data


def get_correct_answers_by_day(lessons_stats: QuerySet[LessonStats]) -> dict:
    correct_answers_by_day = {}
    for lesson_stats in lessons_stats:
        date_str = lesson_stats.date.strftime('%Y-%m-%d')
        correct_answers_by_day[date_str] = lesson_stats.correct_answers

    return correct_answers_by_day


def get_calendar_data_for_period(
        correct_answers_by_day: dict,
        period: Period) -> list[tuple]:
    calendar_data = []
    current_date = period[0]
    while current_date <= period[1]:
        date_str = current_date.strftime('%Y-%m-%d')
        correct_answers = correct_answers_by_day.get(date_str, 0)
        calendar_data.append({
            'date': current_date,
            'correctAnswers': correct_answers,
        })
        current_date += timedelta(days=1)

    return calendar_data
