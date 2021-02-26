from modeltranslation.translator import register, TranslationOptions
from photologue.models import Gallery, Photo
# from .models import GalleryEntry


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title', 'caption',)
