from rest_framework import serializers
from users.serializers import RegisterNewUser
from Missions.serializers import missionSerializer
from .models import *

class medicSerializer(serializers.ModelSerializer):
    healer = RegisterNewUser(read_only=True,many=False)
    healed = RegisterNewUser(read_only=True,many=False)
    mission = missionSerializer(read_only=True,many=False)
    
    class Meta:
        model = medic
        fields ='__all__'
        


class unconsciousSerializer(serializers.ModelSerializer):
    unit = RegisterNewUser(read_only=True,many=False)
    mission = missionSerializer(read_only=True,many=False)
    
    class Meta:
        model = unconscious
        fields ='__all__'
        


class shootsFiredSerializer(serializers.ModelSerializer):
    unit = RegisterNewUser(read_only=True,many=False)
    mission = missionSerializer(read_only=True,many=False)
    
    class Meta:
        model = shootsfired
        fields ='__all__'

        
        