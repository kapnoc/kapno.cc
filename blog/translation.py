from modeltranslation.translator import register, TranslationOptions

from .models import BlogPage


@register(BlogPage)
class BlogPageTranslationOptions(TranslationOptions):
    fields = ('body', 'description', 'title')
