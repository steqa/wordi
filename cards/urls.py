from django.urls import path

from . import views

urlpatterns = [
    path('', views.cards, name='cards'),
]
