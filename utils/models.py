from django.db import models
from martor.models import MartorField


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'"{self.name}" (tag {self.pk})'


class MarkdownPage(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    body = MartorField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'"{self.title}" (page {self.pk})'

    class Meta:
        abstract = True
