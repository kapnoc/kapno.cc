from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer

from django_kapnoc.models import Image
from .models import GalleryEntry


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name_unique', 'description', 'image_display', )
    search_fields = ('name_unique', 'description')
    list_per_page = 25

    @mark_safe
    def image_display(self, obj):
        return '<a href="{0}"><img src="{0}"></a>'.format(get_thumbnailer(obj.image)['admin_small'].url)


class ImageChoiceField(forms.ModelChoiceField):
    @mark_safe
    def label_from_instance(self, obj):
        thumb = get_thumbnailer(obj.image)["admin_small"].url
        return f'<p>{obj.name_unique}: <img src="{thumb}"/></p>'


class GalleryEntryAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'image':
            return ImageChoiceField(queryset=Image.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(GalleryEntry, GalleryEntryAdmin)
admin.site.unregister(Image)
admin.site.register(Image, ImageAdmin)
