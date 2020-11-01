from django.urls import path

from . import views

app_name = "gallery"
urlpatterns = [
    path('', views.index, name='index'),
    path('entry/<int:pk>', views.entry_pk, name='entry_pk'),
]
