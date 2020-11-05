from modeltranslation.translator import register, TranslationOptions

from django_kapnoc.models import Tag


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)
