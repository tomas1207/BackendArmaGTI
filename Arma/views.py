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
from users.models import NewUser
from users.serializers import RegisterNewUser
from django.db.models import Count

from rest_framework_simplejwt.authentication import JWTAuthentication as jwt

# Create your views here.

class MedicStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        return Response(endpoints.NormalEndPoint(self,medic,request,medicSerializer,{'healer_id':request.user.steamID,'mission':request.GET.get('mission')}),status=status.HTTP_200_OK)


class unconsciousStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        
        serialiedData = pagintes.paginatefunc(self,unconscious,request,unconsciousSerializer,{'unit_id':request.user.steamID})
        kwargs ={"DeadCount" : triggerHappy(self,serialiedData.data)}
        return Response(endpoints.NormalEndPoint(self,unconscious,request,unconsciousSerializer,{'unit_id':request.user.id},**kwargs),status=status.HTTP_200_OK)
    

class shootsFiredStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]

    def get(self,request,format='json'):
        print(request.GET.get('mission'))
         
        serialiedData = pagintes.paginatefunc(self,shootsfired,request,shootsFiredSerializer,{'unit_id':request.user.steamID})
        kwargs ={"triggerHappy" : triggerHappy(self,shootsfired,'unit')}
        print(kwargs["triggerHappy"])
        return Response(endpoints.NormalEndPoint(self,shootsfired,request,shootsFiredSerializer,{'mission':request.GET.get('mission')},**kwargs),status=status.HTTP_200_OK)

        
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

def triggerHappy(self,model,fieldname):
    data = shootsfired.objects.values('unit').annotate(triggerHappy=Count('unit'))

    
    for id in data:
        userdata = NewUser.objects.filter(steamID=int(id['unit'])).first()
        print(userdata.user_name)
        serialDatauser = RegisterNewUser(userdata,many=False)
        id['unit'] = serialDatauser.data
        
    return data

        