from django.urls import path, re_path, include

app_name = 'tes'
urlpatterns = [
    # API
    path('api/v1/', include('tes.api.urls')),
]



