from rest_framework import serializers

from .models import Event

class EventSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('event_name', 'event_id', 'image', 'tickets_booked', 'tickets_left')