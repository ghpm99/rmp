from rest_framework import viewsets
from media_socket.models import Event
from media_socket.serializer import EventSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
