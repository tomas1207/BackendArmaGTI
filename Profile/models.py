from django.db import models
from users import models  as md
from django.utils import timezone

# Create your models here.
class info(models.Model):
    steamID= models.TextField()
    vestName = models.CharField(max_length=25)
    birthDay = models.DateTimeField()
    realName = models.TextField()
    age = models.IntegerField()
    loginUser = models.ForeignKey(md.NewUser, on_delete=models.CASCADE)


        

