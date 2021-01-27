from rest_framework import serializers
from users.serializers import RegisterNewUser
from .models import *

class medicSerializer(serializers.ModelSerializer):
    healer = RegisterNewUser(read_only=True,many=False)
    class Meta:
        model = medic
        fields ='__all__'


