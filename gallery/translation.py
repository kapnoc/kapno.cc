from modeltranslation.translator import register, TranslationOptions
from .models import GalleryEntry


@register(GalleryEntry)
class GalleryEntryTranslationOptions(TranslationOptions):
    fields = ('label', 'description',)
