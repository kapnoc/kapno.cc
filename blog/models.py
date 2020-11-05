from django.db import models

from django_kapnoc.models import MarkdownPage


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'"{self.name}" (tag)'


class BlogPage(MarkdownPage):
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        app_label = 'blog'
