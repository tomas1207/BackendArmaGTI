from rest_framework import serializers
from campaign.serializers import campaignSerializer
from users.serializers import RegisterNewUser
from .models import *

class missionSerializer(serializers.ModelSerializer):
    user = RegisterNewUser(read_only=True,many=False)
    campaign = campaignSerializer(read_only=True,many=False)
    joined = RegisterNewUser(read_only=True,many=True)
    class Meta:
        model = missions
        fields ='__all__'
