from django.urls import path
from . import views

urlpatterns = [
    path('webhook', views.pusher_webhook, name='pusher_webhook')
]
