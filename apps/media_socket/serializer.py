from django.db.models import fields
from rest_framework import serializers
from media_socket.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
