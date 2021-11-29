from posixpath import basename
from django.urls import path
from . import views


urlpatterns = [
    path('', views.socket, name='socket')
]
