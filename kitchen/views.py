from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from utils.models import Tag
from .models import KitchenPage


class KitchenPageListView(ListView):
    model = KitchenPage
    template_name = 'kitchen/kitchenpage-list.html'

    def get_queryset(self):
        if self.kwargs.get('tag', None):
            self.tag = get_object_or_404(Tag, name=self.kwargs['tag'])
            return self.tag.kitchenpage_set.all()
        else:
            self.tag = None
            return KitchenPage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.filter(
            kitchenpage__isnull=False,
        )[:]
        context['title'] = f"{_('Kitchen')}"
        context['tags'] = tags
        return context


class KitchenPageDetailView(DetailView):
    model = KitchenPage
    template_name = 'kitchen/kitchenpage-detail.html'
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.title} - {_('Kitchen')}"
        return context
