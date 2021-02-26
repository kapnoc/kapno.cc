from django.urls import path

from .views import BlogPageListView, BlogPageDetailView

app_name = 'blog'
urlpatterns = [
    path('', BlogPageListView.as_view(), name='index'),
    path('tag/<str:tag>', BlogPageListView.as_view(), name='tag'),
    path('page/<int:pk>', BlogPageDetailView.as_view(), name='page'),
]
