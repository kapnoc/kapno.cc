from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

from kapno_cc.models import Tag
from .models import KitchenPage


def index(request):
    tags = Tag.objects.filter(
        kitchenpage__isnull=False,
    )[:]
    pages = KitchenPage.objects.all()[:]
    context = {
        'title': 'Kitchen',
        'tags': tags,
        'pages': pages,
    }
    return render(request, 'kitchen/index.html', context)


def tag_pk(request, pk):
    try:
        queried_tag = Tag.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404("Tag does not exist")
    tags = Tag.objects.filter(
        kitchenpage__isnull=False,
    )[:]
    pages = KitchenPage.objects.all().filter(tags__pk=queried_tag.pk)[:]
    context = {
        'title': f'Kitchen - {queried_tag.name}',
        'tags': tags,
        'pages': pages,
    }
    return render(request, 'kitchen/index.html', context)


def tag_name(request, name):
    try:
        queried_tag = Tag.objects.get(name=name)
    except ObjectDoesNotExist:
        raise Http404("Tag does not exist")
    tags = Tag.objects.filter(
        kitchenpage__isnull=False,
    )[:]
    pages = KitchenPage.objects.all().filter(tags__pk=queried_tag.pk)[:]
    context = {
        'title': f'Kitchen - {queried_tag.name}',
        'tags': tags,
        'pages': pages,
    }
    return render(request, 'kitchen/index.html', context)


def page(request, pk):
    try:
        page = KitchenPage.objects.get(pk=int(pk))
    except ObjectDoesNotExist:
        raise Http404("Page does not exist")
    context = {
        'title': f'Kitchen - {page.title}',
        'page': page,
    }
    return render(request, 'kitchen/page.html', context)
