from modeltranslation.translator import register, TranslationOptions
from photologue.models import Gallery, Photo


# TODO: the translation fields are not created by makemigrations, to be fixed

# @register(Gallery)
# class GalleryTranslationOptions(TranslationOptions):
#     fields = ('title', 'description',)


# @register(Photo)
# class PhotoTranslationOptions(TranslationOptions):
#     fields = ('title', 'caption',)
