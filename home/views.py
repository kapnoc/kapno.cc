from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

from .models import HomePage


def index(request):
    pages = HomePage.objects.all()
    context = {
        'title': _('Home'),
        'pages': pages,
    }
    return render(request, 'home/index.html', context)
