from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import LessonStats
from .utils import get_last_consecutive_days, get_today_lesson_complete


@login_required
def stats(request):
    lesson_stats = LessonStats.objects.filter(
        user=request.user).order_by('-id')[:1]
    last_consecutive_days = get_last_consecutive_days(lesson_stats)
    today_lesson_complete = get_today_lesson_complete(lesson_stats)

    context = {
        'last_consecutive_days': last_consecutive_days,
        'today_lesson_complete': today_lesson_complete
    }
    return render(request, 'stats/stats.html', context)
