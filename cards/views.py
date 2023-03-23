import json

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render
from pydantic import ValidationError

from accounts.utils import get_absolute_url

from .models import Card, CardImages
from .utils import (create_and_get_card_images_without_save,
                    create_and_get_card_without_save,
                    delete_card_images_directory)


@login_required
def cards(request):
    cards = Card.objects.filter(user=request.user.id)
    cards_images = CardImages.objects.filter(card__in=cards)
    context = {
        'cards': cards,
        'cards_images': cards_images,
    }
    if request.method == 'DELETE':
        card_id = request.GET.get('cardID')
        try:
            card = Card.objects.get(user=request.user, pk=card_id)
        except:
            json_status = 400
            error_message = 'Карточка не найдена.'
            json_data = {'msg': error_message}
        else:
            card_pk = card.pk
            card.delete()
            delete_card_images_directory(request.user, card_pk)

            json_status = 200
            redirect_url = get_absolute_url(request, 'cards')
            json_data = {'redirectUrl': redirect_url}

        return JsonResponse(status=json_status, data=json_data)
    return render(request, 'cards/cards.html', context)


@login_required
def add_card(request):
    if request.method == 'POST':
        user = request.user
        post_json = json.dumps(request.POST)
        files_dict = dict(request.FILES.lists())
        try:
            card = create_and_get_card_without_save(
                user=user, json=post_json)
            card_images = create_and_get_card_images_without_save(
                card=card, images_dict=files_dict)
        except ValidationError as e:
            return JsonResponse(status=400, data=e.json(), safe=False)
        else:
            card.save()
            if card_images:
                card_images.save()

            json_status = 200
            redirect_url = get_absolute_url(request, 'cards')
            json_data = {'redirectUrl': redirect_url}
            return JsonResponse(status=json_status, data=json_data)
    return render(request, 'cards/add-card.html')
