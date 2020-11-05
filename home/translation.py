from modeltranslation.translator import register, TranslationOptions
from .models import HomePage


@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    fields = ('body',)
