from django.db import models
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class ExtendedUser(BaseUserManager):

    def create_user(self,username,email,name,password,steamID,vestName):
        if not email:
            raise ValueError('No email providade')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,password=password,steamID=steamID,vestName=vestName)
        user.set_password(password)
        user.save()
        return user
class Newuser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(('email address'),unique=True)
    username = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    startDate = models.DateTimeField(auto_now_add=True)
    isStaff= models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    steamID = models.CharField(max_length=999999999999999999999)
    vestName = models.CharField(max_length=25)

    objects = ExtendedUser()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','steamID','vestName']

    def __str__(self):
        return self.username


