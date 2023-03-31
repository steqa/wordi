from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

from wordi.utils import return_bad_request

from .models import LessonStats
from .utils import (get_calendar_data_for_year, get_last_consecutive_days,
                    get_today_lesson_complete, validate_year)


@login_required
def stats(request):
    if request.method == 'GET' and request.GET.get('year'):
        user = request.user
        year = request.GET.get('year')
        if validate_year(year) is False:
            return return_bad_request(request)
        else:
            calendar_data = get_calendar_data_for_year(user, int(year))
            json_status = 200
            json_data = {'calendarData': calendar_data}

        return JsonResponse(status=json_status, data=json_data)

    lesson_stats = LessonStats.objects.filter(
        user=request.user).order_by('-id')[:1]
    last_consecutive_days = get_last_consecutive_days(lesson_stats)
    today_lesson_complete = get_today_lesson_complete(lesson_stats)

    context = {
        'last_consecutive_days': last_consecutive_days,
        'today_lesson_complete': today_lesson_complete
    }
    return render(request, 'stats/stats.html', context)
