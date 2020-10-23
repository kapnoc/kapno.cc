from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path('', views.index, name='index'),
    path('aled', views.index, name='aled'),
]
