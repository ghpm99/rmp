from django.urls import path
from . import views

urlpatterns = [
    path('send-command', views.send_command_view, name='api_remote_send_command'),
    path('screen-size', views.screen_size_view, name='api_remote_screen_size'),
]
