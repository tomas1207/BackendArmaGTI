# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import *

# Create your views here.
class UserCreator(APIView):
    permission_classes = [AllowAny]
    def post(self,request,format='json'):
        reg_serializer = RegisterNewUser(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                json = reg_serializer.data
                return Response(json,status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class MissionStatus(APIView):
    permission_classes =[IsAuthenticated]
    def get(self,request,format='json'):
        mission = {"Campanha1":{"actived":True,"NofMission":4,"PlayersIds":[1234567789,123456778900]}}
        return Response(mission,status=status.HTTP_200_OK)