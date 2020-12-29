from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterNewUser

# Create your views here.
class CustomUserCreator(APIView):
    """
    docstring
    """
    permission_classes = [AllowAny]
    def post(self,request):
        reg_serializer = RegisterNewUser(request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer,status=status.HTTP_400_BAD_REQUEST)