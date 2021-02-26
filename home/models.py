from django.db import models


from utils.models import Tag, MarkdownPage


class HomePage(MarkdownPage):
    tags = models.ManyToManyField(Tag)

    class Meta:
        app_label = 'home'
