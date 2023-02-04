from rest_framework import serializers

from .models import User

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'contact')