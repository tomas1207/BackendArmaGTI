from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from .serializers import RegisterNewUser
from django.core import mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .models import NewUser as nu
from django.http import HttpResponseRedirect
import jwt
from  django.conf import settings

# Create your views here.
class UserCreator(APIView):
    permission_classes = [AllowAny]
    def post(self,request,format='json'):
        reg_serializer = RegisterNewUser(data=request.data)
        print(reg_serializer.is_valid())
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                json = reg_serializer.data
                token = RefreshToken.for_user(newuser)
                self.sendEmail(token,request,json)
                return Response(json,status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def sendEmail(self, token, request,json):
        current_site = get_current_site(request).domain
        relativeLink = reverse('emailVerify')
        linkforactivate = 'http://'+ current_site+relativeLink+'?token='+str(token.access_token)
        email = mail.EmailMessage(subject="Activate account GTIFenix",body=linkforactivate,to=[json['email']],from_email='no-reply@gtifenix.com')

        return email.send()

class login(APIView):
    permission_classes = [AllowAny]
    def post(self,request,format='json'):
        email = request.data["email"]
        password = request.data["password"]
        print(password,email)
        user = nu.objects.filter(email=email).first()
        if not user:
            raise  AuthenticationFailed("user not found")
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            jsonjwt = {
                'userdata': RegisterNewUser(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(jsonjwt, status=status.HTTP_200_OK)
        return Response({"msg":"usernotfound"}, status=status.HTTP_200_OK)
      
class Logout(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        print(request.POST.get("refresh"))
        Refresh_token = request.POST.get("refresh")
        token = RefreshToken(Refresh_token)
        token.blacklist()
        return Response("Successful Logout", status=status.HTTP_200_OK)

class VerifyEmail(APIView):
    def get(self,request):
        token = request.GET.get('token')
        try:
            payload= jwt.decode(token, settings.SECRET_KEY,algorithms="HS256")
            user = nu.objects.get(id=payload['user_id'])

            user.is_active = True
            user.save()
                        
            return HttpResponseRedirect('http://localhost:4200/home')
        except jwt.ExpiredSignatureError as identifier:
            pass
        
