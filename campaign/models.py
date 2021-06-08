from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class campaign(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    name = models.TextField()
    ismaincampaing = models.BooleanField()
    description = models.TextField(blank=True)
    status = models.BooleanField()
    image = models.ImageField(blank=True)