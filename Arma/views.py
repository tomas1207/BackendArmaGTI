# Create your views here.
from django.shortcuts import render
from CoreAppClass.normalEndpoint import endpoints
from CoreAppClass.paginate import pagintes
from django.core import serializers
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import *
from rest_framework.pagination import LimitOffsetPagination
from .models import medic
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication as jwt

# Create your views here.

class MedicStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        return Response(endpoints.NormalEndPoint(self,medic,request,medicSerializer,{'healer_id':request.user.steamID,'mission':request.GET.get('mission')}),status=status.HTTP_200_OK)


class unconsciousStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        
        serialiedData = pagintes.paginatefunc(self,unconscious,request,unconsciousSerializer,{'unit_id':request.user.id})
        kwargs ={"DeadCount" : DeadCounts(self,serialiedData.data)}
        return Response(endpoints.NormalEndPoint(self,unconscious,request,unconsciousSerializer,{'unit_id':request.user.id},**kwargs),status=status.HTTP_200_OK)
    

class shootsFiredStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]

    def get(self,request,format='json'):
        return Response(endpoints.NormalEndPoint(self,shootsfired,request,shootsFiredSerializer,{'unit_id':request.user.id}),status=status.HTTP_200_OK)

        
def DeadCounts(self,data):
    i= 0
    deadsCounts = 0
    
    while i < len(data):

        current = data[i]["state"] 
        prev = data[i-1]["state"]

        if i == 0:
            prev = False
        
        if current and prev:
            deadsCounts += 1
        
        i += 1
    
    if data[-1]["state"]:
        deadsCounts  += 1

    return deadsCounts

        