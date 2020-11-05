from django.db import models


from django_kapnoc.models import MarkdownPage


class HomePage(MarkdownPage):
    class Meta:
        app_label = 'home'
