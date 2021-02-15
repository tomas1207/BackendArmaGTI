from django.db import models
from Missions.models import  missions
from django.conf import settings
from django.utils import timezone

# Create your models here.
class shootsfired(models.Model):
    unit = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="unit",to_field='steamID',null=True)
    weapon = models.TextField()
    muzzle = models.TextField()
    mode = models.TextField()
    ammo = models.TextField()
    magazine = models.TextField()
    projectile = models.TextField()
    mission = models.ForeignKey(missions,on_delete=models.CASCADE,related_name="mission",null=True)

        
class unconscious(models.Model):
    unit = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="Uncoscious",to_field='steamID',null=True)
    state = models.BooleanField()
    createdat = models.DateTimeField()
    updateat = models.DateTimeField()
    mission = models.ForeignKey(missions,on_delete=models.CASCADE,related_name="mission_unconscious",null=True)

class kills(models.Model):
    killer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="killer",to_field='steamID',null=True)
    weapon= models.TextField(default=0)
    killed= models.TextField(default=0)
    distance= models.TextField(default=0)
    mission = models.ForeignKey(missions,on_delete=models.CASCADE,related_name="mission_kills",null=True)


class medic(models.Model):
    healer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="healer",to_field='steamID',null=True)
    healed= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="healed",to_field='steamID',null=True)
    hitLocation= models.TextField()
    typeOfHeal= models.TextField()
    mission = models.ForeignKey(missions,on_delete=models.CASCADE,related_name="mission_medic",null=True)

