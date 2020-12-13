from django.contrib import admin
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer

from django_kapnoc.models import Image
from .models import GalleryEntry


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name_unique', 'description', 'image_display', )
    search_fields = ('name_unique', 'description')
    list_per_page = 25

    def image_display(self, obj):
        return mark_safe('<a href="{0}"><img src="{0}"></a>'.format(get_thumbnailer(obj.image)['admin_small'].url))


admin.site.register(GalleryEntry)
admin.site.unregister(Image)
admin.site.register(Image, ImageAdmin)
