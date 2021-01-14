# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import *

# Create your views here.
        

class MissionStatus(APIView):
    permission_classes =[IsAuthenticated]
    def get(self,request,format='json'):
        mission = {"Campanha1":{"actived":True,"NofMission":4,"PlayersIds":[1234567789,123456778900]}}
        return Response(mission,status=status.HTTP_200_OK)