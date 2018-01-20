from django.urls import path, re_path

from . import views

app_name = 'peserta'
urlpatterns = [
    path('', views.index, name='index'),
    path('registrasi/', views.registrasi, name='registrasi'),
    re_path(r'^registrasi/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/aktifasi/$',
            views.aktifasi, name='aktifasi'),
]
