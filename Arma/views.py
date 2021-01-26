# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import *
from .models import medic
from .serializers import *
from django.core import serializers
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication as jwt

# Create your views here.
        

class MissionStatus(APIView):
    permission_classes =[IsAuthenticated]
    def get(self,request,format='json'):
        mission = {"Campanha1":{"actived":True,"NofMission":4,"PlayersIds":[1234567789,123456778900]}}
        return Response(mission,status=status.HTTP_200_OK)


class MedicStatus(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        medics = medic.objects.all().filter(healer=request.user.id)
        finalData = medicSerializer(medics, many=True)
        return JsonResponse(finalData.data,status=status.HTTP_200_OK, safe=False)
        