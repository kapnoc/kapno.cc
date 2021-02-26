from django.urls import path
from .views import NewGalleryListView, NewGalleryDetailView, NewPhotoDetailView

app_name = "gallery"
urlpatterns = [
    path('', NewGalleryListView.as_view(), name='gallery-list'),
    path('category/<slug:slug>', NewGalleryDetailView.as_view(),
         name='gallery-detail'),
    path('photo/<slug:slug>', NewPhotoDetailView.as_view(),
         name='photo-detail'),
]
