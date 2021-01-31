from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterNewUser
from django.core import mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .models import NewUser as nu
import jwt
from  django.conf import settings

# Create your views here.
class UserCreator(APIView):
    permission_classes = [AllowAny]
    def post(self,request,format='json'):
        reg_serializer = RegisterNewUser(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                json = reg_serializer.data
                token = RefreshToken.for_user(newuser)
                current_site = get_current_site(request).domain
                relativeLink = reverse('emailVerify')
                linkforactivate = 'http://'+ current_site+relativeLink+'?token='+str(token.access_token)
                email = mail.EmailMessage(subject="Activate account",body=linkforactivate,to=[json['email']],from_email='no-reply@gtifenix.com')
                email.send()
                return Response(json,status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(APIView):
    def get(self,request):
        token = request.GET.get('token')
        try:
            payload= jwt.decode(token, settings.SECRET_KEY,algorithms="HS256")
            user = nu.objects.get(id=payload['user_id'])

            user.is_active = True
            user.save()
                        
            return Response('Done', status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            pass
        
