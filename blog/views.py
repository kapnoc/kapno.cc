from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from utils.models import Tag
from .models import BlogPage


class BlogPageListView(ListView):
    model = BlogPage
    template_name = 'blog/blogpage-list.html'

    def get_queryset(self):
        if self.kwargs.get('tag', None):
            self.tag = get_object_or_404(Tag, name=self.kwargs['tag'])
            return self.tag.blogpage_set.all()
        else:
            self.tag = None
            return BlogPage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.filter(
            blogpage__isnull=False,
        )[:]
        context['title'] = f"{_('Blog')}"
        context['tags'] = tags
        return context


class BlogPageDetailView(DetailView):
    model = BlogPage
    template_name = 'blog/blogpage-detail.html'
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.title} - {_('Blog')}"
        return context
