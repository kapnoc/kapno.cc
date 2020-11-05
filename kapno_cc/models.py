from django.db import models

from django_kapnoc.models import Tag as AbsTag


class Tag(AbsTag):
    class Meta:
        app_label = 'kapno_cc'
