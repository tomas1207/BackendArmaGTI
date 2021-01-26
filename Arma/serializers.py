from rest_framework import serializers
from .models import *

class medicSerializer(serializers.ModelSerializer):
    class Meta:
        model = medic
        fields ='__all__'
        depth=1


