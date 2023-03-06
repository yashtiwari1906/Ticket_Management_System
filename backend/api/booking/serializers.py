from rest_framework import serializers

from .models import Booking, Seats

class BookingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seats
        fields = ('event', 'row', 'col', 'booked')