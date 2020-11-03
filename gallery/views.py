from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from .models import GalleryEntry


def index(request):
    entries = GalleryEntry.objects.filter(parent=None)[:]
    context = {
        'title': _('Gallery'),
        'at_gallery_home': True,
        'entries': entries,
    }
    return render(request, 'gallery/index.html', context)


def entry_pk(request, pk):
    if pk == None:
        return redirect(index)
    try:
        elem = GalleryEntry.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404(_('Gallery element does not exist'))
    entries = GalleryEntry.objects.filter(parent=pk)
    if entries.count() == 0:
        pass
    try:
        prev = elem.get_previous_by_created_at(parent=elem.parent)
    except ObjectDoesNotExist:
        prev = None
    try:
        next = elem.get_next_by_created_at(parent=elem.parent)
    except ObjectDoesNotExist:
        next = None
    # switch next and prev as display order makes more sense
    prev, next = next, prev
    context = {
        'title': _('Gallery') + ' - ' + elem.label,
        'elem': elem,
        'parent': elem.parent,
        'prev': prev,
        'next': next,
        'entries': entries,
    }
    return render(request, 'gallery/index.html', context)
