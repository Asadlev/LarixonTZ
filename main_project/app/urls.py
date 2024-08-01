from django.urls import path
from .views import AdvertListView, AdvertDetailView

urlpatterns = [
    path('api/advert-list/', AdvertListView.as_view(), name='advert-list'),
    path('api/advert/<int:advert_pk>/', AdvertDetailView.as_view(), name='advert-detail'),
]
