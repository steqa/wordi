import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from pydantic import ValidationError

from .models import Card, CardImages
from .utils import (create_and_get_card_images_without_save,
                    create_and_get_card_without_save)


@login_required
def cards(request):
    cards = Card.objects.filter(user=request.user.id)
    cards_images = CardImages.objects.filter(card__in=cards)
    context = {
        'cards': cards,
        'cards_images': cards_images,
    }
    return render(request, 'cards/cards.html', context)


@login_required
def add_card(request):
    if request.method == 'POST':
        user = request.user
        input_post_json = json.dumps(request.POST)
        input_files_dict = dict(request.FILES.lists())
        try:
            card = create_and_get_card_without_save(
                user=user, json=input_post_json)
            card_images = create_and_get_card_images_without_save(
                card=card, images_dict=input_files_dict)
        except ValidationError as e:
            response_status = 400
            response_data = e.json().replace(
                'field required', 'Обязательное поле.')
            return JsonResponse(status=response_status,
                                data=response_data, safe=False)
        else:
            card.save()
            if card_images:
                card_images.save()
            return JsonResponse(status=200,
                                data=json.dumps({
                                    'redirectUrl': request.build_absolute_uri(
                                        reverse('cards')
                                    )
                                }), safe=False)
    return render(request, 'cards/add-card.html')
