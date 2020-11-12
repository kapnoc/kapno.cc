from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _

from blog.models import Tag
from .models import BlogPage


def index(request):
    tags = Tag.objects.filter(
        blogpage__isnull=False,
    )[:]
    pages = BlogPage.objects.all()[:]
    context = {
        'title': _('Blog'),
        'tags': tags,
        'pages': pages,
    }
    return render(request, 'blog/index.html', context)


def tag_pk(request, pk):
    try:
        queried_tag = Tag.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404("Tag does not exist")
    tags = Tag.objects.filter(
        blogpage__isnull=False,
    )[:]
    pages = BlogPage.objects.all().filter(tags__pk=queried_tag.pk)[:]
    context = {
        'title': f'{_("Blog")} - {queried_tag.name}',
        'tags': tags,
        'pages': pages,
    }
    return render(request, 'blog/index.html', context)


def tag_name(request, name):
    try:
        queried_tag = Tag.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Http404("Tag does not exist")
    tags = Tag.objects.filter(
        blogpage__isnull=False,
    )[:]
    pages = BlogPage.objects.all().filter(tags__pk=queried_tag.pk)[:]
    context = {
        'title': f'{_("Blog")} - {queried_tag.name}',
        'tags': tags,
        'pages': pages,
    }
    return render(request, 'blog/index.html', context)


def page(request, pk):
    try:
        page = BlogPage.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404("Page does not exist")
    context = {
        'title': f'{_("Blog")} - {page.title}',
        'page': page,
    }
    return render(request, 'blog/page.html', context)
