import json

from django.contrib.auth.decorators import login_required
from django.http.multipartparser import MultiPartParser
from django.http.response import JsonResponse
from django.shortcuts import render
from pydantic import ValidationError

from accounts.utils import get_absolute_url

from .data_classes import CardData, CardImagesData
from .models import Card, CardImages
from .utils import (create_card, create_card_images,
                    delete_card_images_directory, update_card,
                    update_card_images)


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

    if request.method == 'PUT':
        user = request.user
        card_id = int(request.GET.get('cardID'))
        if Card.objects.filter(user=user, pk=card_id).exists():
            parse_request = MultiPartParser(
                request.META, request, request.upload_handlers).parse()
            post_json = json.dumps(parse_request[0])
            files_dict = dict(parse_request[1])
            try:
                card_data = CardData.parse_raw(post_json)
                card_images_data = CardImagesData.parse_obj(files_dict)
            except ValidationError as e:
                return JsonResponse(status=400, data=e.json(), safe=False)
            else:
                card = update_card(card_id, card_data)
                try:
                    card_images = CardImages.objects.get(card_id=card_id)
                except:
                    if card_images_data.is_not_empty():
                        card_images = create_card_images(
                            card, card_images_data)
                else:
                    if card_images_data.is_not_empty():
                        card_images = update_card_images(
                            card_images.pk, card_images_data)
                    else:
                        card_images.delete()
                        delete_card_images_directory(user, card_id)

                json_status = 200
                redirect_url = get_absolute_url(request, 'cards')
                json_data = {'redirectUrl': redirect_url}
        else:
            json_status = 400
            error_message = 'Карточка не найдена.'
            json_data = {'msg': error_message}

        return JsonResponse(status=json_status, data=json_data)
    return render(request, 'cards/cards.html', context)


@login_required
def add_card(request):
    if request.method == 'POST':
        user = request.user
        post_json = json.dumps(request.POST)
        files_dict = dict(request.FILES.lists())
        try:
            card_data = CardData.parse_raw(post_json)
            card_images_data = CardImagesData.parse_obj(files_dict)
        except ValidationError as e:
            return JsonResponse(status=400, data=e.json(), safe=False)
        else:
            card = create_card(user, card_data)
            if card_images_data.is_not_empty():
                card_images = create_card_images(card, card_images_data)

            json_status = 200
            redirect_url = get_absolute_url(request, 'cards')
            json_data = {'redirectUrl': redirect_url}
            return JsonResponse(status=json_status, data=json_data)
    return render(request, 'cards/add-card.html')
