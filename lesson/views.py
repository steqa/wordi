from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cards.models import Card, CardImages


@login_required
def lesson(request):
    cards = Card.objects.filter(user=request.user.id).order_by('?')[:10]
    cards_images = CardImages.objects.filter(card__in=cards)
    context = {
        'cards': cards,
        'cards_images': cards_images,
    }
    return render(request, 'lesson/lesson.html', context)
