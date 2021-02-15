from rest_framework import serializers
from users.serializers import RegisterNewUser
from .models import *

class missionSerializer(serializers.ModelSerializer):
    user = RegisterNewUser(read_only=True,many=False)
    class Meta:
        model = missions
        fields ='__all__'