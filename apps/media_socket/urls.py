
from django.urls import include, path
from rest_framework import routers

from media_socket.views import EventsViewSet

router = routers.DefaultRouter()
router.register('event', EventsViewSet, basename='Event')

urlpatterns = [
    path('', include(router.urls))
]
