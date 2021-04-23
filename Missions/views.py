from CoreAppClass.normalEndpoint import endpoints 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import missions
from users.models import  NewUser
from .serializers import missionSerializer
from rest_framework.permissions import *
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.
class missionsStatus(APIView,LimitOffsetPagination):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        return Response(endpoints.NormalEndPoint(self,missions,request,missionSerializer,{'user_id':request.user.id,'campaign':request.GET.get('campaign')}),status=status.HTTP_200_OK)
        
    def post(self,request,format='json'):
        print(type(request.user))
        missioncreate = missions(user=request.user)

        serialedData = missionSerializer(missioncreate,data = request.data)
        if serialedData.is_valid():
            serialedData.save()
            return Response(serialedData.data)
        return Response(serialedData.errors)
