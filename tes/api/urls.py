from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

from .views import (
    SoalView,
    SoalDetailView,
    SoalKegiatanView,
)

urlpatterns = [
    path('token-auth/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),

    # endpoint
    path('', SoalView.as_view(), name='index'),
    path('<int:pk>/', SoalDetailView.as_view(), name='detail'),
    path('<str:kegiatan>/', SoalKegiatanView.as_view(), name='kegiatan'),
]