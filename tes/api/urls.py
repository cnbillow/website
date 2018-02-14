from django.urls import path

from .views import (
    SoalView,
    SoalDetailView,
    SoalKegiatanView,
)

urlpatterns = [
    path('', SoalView.as_view(), name='index'),
    path('<int:pk>/', SoalDetailView.as_view(), name='detail'),
    path('<str:kegiatan>/', SoalKegiatanView.as_view(), name='kegiatan'),
]