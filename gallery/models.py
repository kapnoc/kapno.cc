from django.db import models

from django_kapnoc.models import Image, Tag


class GalleryEntry(models.Model):
    image = models.ManyToManyField(Image)
    label = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'GalleryEntry', blank=True, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.label} (GalleryEntry)'
