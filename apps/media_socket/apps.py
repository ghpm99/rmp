from django.apps import AppConfig

from apps.media_socket.listeners import register_listeners


class MediaSocketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'media_socket'

    def ready(self):
        register_listeners()
