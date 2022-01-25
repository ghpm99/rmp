from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='media'),
    path('get-media', views.get_media_files, name='media_api_files'),
]
