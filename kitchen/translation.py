from modeltranslation.translator import register, TranslationOptions

from .models import KitchenPage


@register(KitchenPage)
class KitchenPageTranslationOptions(TranslationOptions):
    fields = ('body', 'description', 'title')
