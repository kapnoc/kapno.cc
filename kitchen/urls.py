from django.urls import path

from .views import KitchenPageListView, KitchenPageDetailView

app_name = 'kitchen'
urlpatterns = [
    path('', KitchenPageListView.as_view(), name='index'),
    path('tag/<str:tag>', KitchenPageListView.as_view(), name='tag'),
    path('page/<int:pk>', KitchenPageDetailView.as_view(), name='page'),
]
