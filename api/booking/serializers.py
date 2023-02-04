from rest_framework import serializers

from .models import Booking

class BookingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('ticket', 'event', 'user_id')