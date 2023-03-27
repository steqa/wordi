import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

from cards.models import Card, CardImages
from wordi.utils import return_bad_request

from .utils import (get_correct_answers, get_feedback_and_num_correct,
                    validate_user_answers)


@login_required
def lesson(request):
    cards = Card.objects.filter(user=request.user.id).order_by('?')[:10]
    cards_images = CardImages.objects.filter(card__in=cards)
    context = {
        'cards': cards,
        'cards_images': cards_images,
    }

    if request.method == 'POST':
        try:
            user_answers = json.loads(request.POST.get('answers'))
            if validate_user_answers(user_answers, cards) is False:
                raise Exception
        except:
            return return_bad_request(request)

        correct_answers = get_correct_answers(cards)
        feedback, num_correct = get_feedback_and_num_correct(
            user_answers, correct_answers)

        json_status = 200
        json_data = {'feedback': feedback,
                     'correct': num_correct,
                     'total': len(cards)}
        return JsonResponse(status=json_status, data=json_data)
    return render(request, 'lesson/lesson.html', context)
