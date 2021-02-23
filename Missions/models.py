from django.db import models
from campaign.models import campaign
from django.conf import settings
from django.utils import timezone

# Create your models here.
class missions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="user")
    typeofmission = models.TextField()
    missionName = models.TextField()
    briefing = models.TextField()
    solts = models.TextField()
    campaign = models.ForeignKey(campaign,on_delete=models.CASCADE)


        
