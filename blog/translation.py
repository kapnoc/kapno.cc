from modeltranslation.translator import register, TranslationOptions

from blog.models import Tag
from .models import BlogPage


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(BlogPage)
class BlogPageTranslationOptions(TranslationOptions):
    fields = ('body', 'description', 'title')
