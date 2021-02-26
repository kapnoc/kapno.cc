from django.utils.translation import gettext as _
from django.views.generic import ListView

from .models import HomePage


class HomePageView(ListView):
    model = HomePage
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{_('Home')}"
        return context
