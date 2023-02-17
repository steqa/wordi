from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from cards.models import Card, CardImages
from wordi.tests.mixins import (TestPagesShowCorrectContext,
                                TestPagesUsesCorrectTemplateMixin)

User = get_user_model()


class CardsPagesTests(TestCase, TestPagesUsesCorrectTemplateMixin, TestPagesShowCorrectContext):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345',
        )
        cls.card = Card.objects.create(
            user=cls.user,
            front_text='тестовый текст на передней стороне',
            back_text='тестовый текст на задней стороне',
        )
        cls.cardImages = CardImages.objects.create(
            card=cls.card,
        )
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)
        cls.templates_pages_names = {
            'cards/cards.html': reverse('cards'),
        }
        cls.pages_and_context_keys_with_values = {
            'cards': {
                'cards': cls.card,
                'cards_images': cls.cardImages,
            },
        }

    def test_pages_uses_correct_template(self):
        super().run_pages_uses_correct_template_test()

    def test_pages_show_correct_context(self):
        super().run_pages_show_correct_context_test()
