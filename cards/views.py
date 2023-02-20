from django.shortcuts import render

from .models import Card, CardImages


def cards(request):
    cards = Card.objects.filter(user=request.user.id)
    cards_images = CardImages.objects.filter(card__in=cards)
    context = {
        'cards': cards,
        'cards_images': cards_images,
    }
    return render(request, 'cards/cards.html', context)


def add_card(request):
    return render(request, 'cards/add-card.html')
