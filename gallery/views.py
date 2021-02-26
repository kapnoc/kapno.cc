from django.views.generic import ListView, DetailView
from photologue.models import Gallery, Photo
from django.utils.translation import gettext as _


class NewPhotoDetailView(DetailView):
    model = Photo
    template_name = 'gallery/photo-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.title} - {_('Gallery')}"
        return context


class NewGalleryDetailView(DetailView):
    model = Gallery
    template_name = 'gallery/gallery-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.title} - {_('Gallery')}"
        return context


class NewGalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/gallery-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Gallery")
        return context
