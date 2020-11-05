from django.db import models

from django_kapnoc.models import MarkdownPage


class KitchenPage(MarkdownPage):
    description = models.TextField()

    class Meta:
        app_label = 'blog'
