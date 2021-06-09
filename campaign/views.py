from CoreAppClass.normalEndpoint import endpoints 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import campaign
from .serializers import campaignSerializer
from CoreAppClass import paginate
from rest_framework.permissions import *
from Missions.models import *
from Missions.serializers import *
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.
class Campaign(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        return Response(endpoints.NormalEndPoint(self,campaign,request,campaignSerializer,{'user_id':request.user.id}),status=status.HTTP_200_OK)
        
    def post(self,request,format='json'):
        missioncreate = campaign(user=request.user)
        
        serialedData = campaignSerializer(missioncreate,data = request.data)
        if serialedData.is_valid():
            serialedData.save()
            return Response(serialedData.data)
        return Response(serialedData.errors)

class CampaignCount(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):

        count = missions.objects.filter(campaign=request.GET.get("campaign")).count()
        kwargs = {"count":count}
        return Response(kwargs,status=status.HTTP_200_OK)