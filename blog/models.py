from django.db import models

from utils.models import Tag, MarkdownPage


class BlogPage(MarkdownPage):
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        app_label = 'blog'
