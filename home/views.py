from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _


def index(request):
    context = {
        'title': _('Home'),
    }
    return render(request, 'home/index.html', context)
