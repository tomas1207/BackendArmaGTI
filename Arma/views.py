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
from .models import *
from .serializers import *
from users.models import NewUser
from users.serializers import RegisterNewUser
from django.db.models import Count

from rest_framework_simplejwt.authentication import JWTAuthentication as jwt

# Create your views here.

class MedicStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        kwargs={
            "mostusedItem":Extradata(self,medic,'typeOfHeal',request.GET.get('mission'),'healer_id'),
            "bestMedic": Extradata(self,medic,'healer_id',request.GET.get('mission'),'healer_id'),
            "holey": Extradata(self,medic,'healed_id',request.GET.get('mission'),'healed_id'),
            "mostShootZone": Extradata(self,medic,'hitLocation',request.GET.get('mission'),'healed_id')
        }
        return Response(endpoints.NormalEndPoint(self,medic,request,medicSerializer,{'mission':request.GET.get('mission')},**kwargs),status=status.HTTP_200_OK)


class unconsciousStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        
        serialiedData = pagintes.paginatefunc(self,unconscious,request,unconsciousSerializer,{'mission':request.GET.get('mission')})
        kwargs ={
            "DeadCount" : DeadCounts(self,serialiedData.data),
            "TheGroundHugger": Extradata(self,unconscious,'unit_id',request.GET.get('mission'),'unit_id')
        }
        return Response(endpoints.NormalEndPoint(self,unconscious,request,unconsciousSerializer,{'mission':request.GET.get('mission')},**kwargs),status=status.HTTP_200_OK)
    
class shootsFiredStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]

    def get(self,request,format='json'):
        kwargs ={
            "TriggerHappy" : Extradata(self,shootsfired,'unit',request.GET.get('mission'),'unit'),
            "mostWeaponUsed":Extradata(self,shootsfired,'weapon',request.GET.get('mission'),'unit'),
            "mostUsedMode":Extradata(self,shootsfired,'mode',request.GET.get('mission'),'unit'),
            "AmmoDispenser":Extradata(self,shootsfired,'ammo',request.GET.get('mission'),'unit')
            }
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

def Extradata(self,model,fieldname,mission,unitName=""):
    data = model.objects.filter(mission=mission).values(fieldname,unitName).annotate(count=Count(fieldname))
    for id in data:
        userdata = NewUser.objects.filter(steamID=int(id[unitName])).first()
        serialDatauser = RegisterNewUser(userdata,many=False)
        id[unitName] = serialDatauser.data
        
    return data
