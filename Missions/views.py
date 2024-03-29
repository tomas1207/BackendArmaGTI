from campaign.models import campaign
from CoreAppClass.normalEndpoint import endpoints 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import missions
from users.models import  NewUser
from .serializers import missionSerializer
from campaign.models import  campaign
from rest_framework.permissions import *
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
import json

# Create your views here.
class missionsStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        return Response(endpoints.NormalEndPoint(self,missions,request,missionSerializer,{'campaign':request.GET.get('campaign')}),status=status.HTTP_200_OK)
        
    def post(self,request,format='json'):
        mycampaign = campaign.objects.filter(id=request.data['campaign']).first()
        missioncreate = missions(campaign=mycampaign,user=request.user)
        serialedData = missionSerializer(missioncreate,data = request.data)
        if serialedData.is_valid():
            serialedData.save()
            return Response(serialedData.data)
        return Response(serialedData.errors)

    def put(self, request,format='json'):
        print(request.data)
        missionid = request.data["id"]
        print(missionid)
        mission = missions.objects.filter(id=missionid).first()
        mission.isfinish = True
        mission.save()
        serialedData = missionSerializer(mission)
        return Response(serialedData.data)
class missionDetails(APIView,LimitOffsetPagination):
    permission_classes=[IsAuthenticated]
    def get(self,request):  
        return Response(endpoints.NormalEndPoint(self,missions,request,missionSerializer,{
            'id':request.GET.get('mission')
        })) 
class missionregistion(APIView,LimitOffsetPagination):
    permission_classes=[IsAuthenticated]
    def post(self,request,format='json'):
        print(request.data)
        user = request.user.id
        missionid = request.data['mission']
        missionObj = missions.objects.get(id=missionid)
        if missionObj.maxsolts != missionObj.joined.count():

            missionObj.joined.add(user)
            missionObj.save()
            return Response(missionSerializer(missionObj).data)
        else:
            return Response({"slots":"Max Slots reached"})