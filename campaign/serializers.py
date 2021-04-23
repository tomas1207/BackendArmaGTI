from rest_framework import serializers
from users.serializers import RegisterNewUser
from .models import *
from Missions.models import missions

class campaignSerializer(serializers.ModelSerializer):
    user = RegisterNewUser(read_only=True,many=False)   
    
    class Meta:
        model = campaign
        fields ='__all__'
        