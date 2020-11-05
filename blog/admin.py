from django.contrib import admin

from .models import BlogPage, Tag

admin.site.register(BlogPage)
admin.site.register(Tag)
