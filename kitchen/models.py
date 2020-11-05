from django.db import models

from django_kapnoc.models import MarkdownPage

from kapno_cc.models import Tag


class KitchenPage(MarkdownPage):
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        app_label = 'blog'
