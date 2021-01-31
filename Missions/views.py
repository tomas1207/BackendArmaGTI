from django.shortcuts import render
from rest_framework.views import APIView
from .models import missions
from .serializers import missionSerializer
from rest_framework.permissions import *
from django.http import JsonResponse
from rest_framework import status
# Create your views here.
class MissionStatus(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format='json'):
        medics = missions.objects.all()

        finalData = missionSerializer(medics, many=True)
        return JsonResponse(finalData.data,status=status.HTTP_200_OK,safe=False)
        