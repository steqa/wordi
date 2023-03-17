from django.urls import path

from . import views

urlpatterns = [
    path('', views.cards, name='cards'),
    path('add/', views.add_card, name='add-card'),
]
