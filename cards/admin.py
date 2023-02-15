from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Card, CardImages


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('user', 'front_text', 'back_text')
    search_fields = ('user', 'front_text', 'back_text')
    list_filter = ('date_created', 'date_updated')
    readonly_fields = ('id', 'date_created', 'date_updated')
    fieldsets = (
        (None,
            {'fields': (
                'id',
                'user',
            )}),
        ('Передняя сторона',
            {'fields': (
                'front_text',
            )}),
        ('Задняя сторона',
            {'fields': (
                'back_text',
            )}),
        ('Важные даты',
            {'fields': (
                'date_created',
                'date_updated',
            )}),
    )


@admin.register(CardImages)
class CardImagesAdmin(admin.ModelAdmin):
    list_display = ('card', 'front_image_preview', 'back_image_preview')
    readonly_fields = ('id', 'front_image_preview_inside',
                       'back_image_preview_inside')
    fieldsets = (
        (None,
            {'fields': (
                'id',
                'card',
            )}),
        ('Передняя сторона',
            {'fields': (
                'front_image',
                'front_image_preview_inside',
            )}),
        ('Задняя сторона',
            {'fields': (
                'back_image',
                'back_image_preview_inside',
            )}),
    )

    def front_image_preview(self, card: Card):
        if card.front_image:
            return mark_safe(f'<img src="{card.front_image.url}" style="max-height: 25px;">')
        else:
            return 'Отсутствует'

    front_image_preview.short_description = 'изображение на передней стороне'

    def back_image_preview(self, card: Card):
        if card.back_image:
            return mark_safe(f'<img src="{card.back_image.url}" style="max-height: 25px;">')
        else:
            return 'Отсутствует'

    back_image_preview.short_description = 'изображение на задней стороне'

    def front_image_preview_inside(self, card: Card):
        if card.front_image:
            return mark_safe(f'<img src="{card.front_image.url}" style="max-height: 200px;">')
        else:
            return 'Отсутствует'

    front_image_preview_inside.short_description = 'просмотр изображения на передней стороне'

    def back_image_preview_inside(self, card: Card):
        if card.back_image:
            return mark_safe(f'<img src="{card.back_image.url}" style="max-height: 200px;">')
        else:
            return 'Отсутствует'

    back_image_preview_inside.short_description = 'просмотр изображения на задней стороне'
