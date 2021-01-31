# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import *
from rest_framework.pagination import LimitOffsetPagination
from .models import medic
from .serializers import *
from django.core import serializers
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication as jwt

# Create your views here.
        
limitOffsetPagination = LimitOffsetPagination()
limitOffsetPagination.default_limit = 1
class MissionStatus(APIView):
    permission_classes =[IsAuthenticated]
    def get(self,request,format='json'):
        mission = {"Campanha1":{"actived":True,"NofMission":4,"PlayersIds":[1234567789,123456778900]}}
        return Response(mission,status=status.HTTP_200_OK)


class MedicStatus(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        medics = medic.objects.all().filter(healer=request.user.steamID,mission=request.data["mission"])

        data = limitOffsetPagination.paginate_queryset(medics,request)
        print(limitOffsetPagination.get_next_link() )
        finalData = medicSerializer(data, many=True)
        data ={
            'pagination':{
                'next':limitOffsetPagination.get_next_link(),
                'previous':limitOffsetPagination.get_previous_link(),
            },
            'data': finalData.data
        }
        return Response(data,status=status.HTTP_200_OK)
        