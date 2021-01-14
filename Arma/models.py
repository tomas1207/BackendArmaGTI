from django.db import models
from users import models  as md
from django.utils import timezone

# Create your models here.
class shootsfired(models.Model):
    unit = models.ForeignKey(md.NewUser, on_delete=models.CASCADE)
    weapon = models.TextField()
    muzzle = models.TextField()
    mode = models.TextField()
    ammo = models.TextField()
    magazine = models.TextField()
    projectile = models.TextField()
    #vehicle = models.TextField()
    createdat = models.DateTimeField()
    updateat = models.DateTimeField()

    
    def __str__(self):
        return self.unit + ' ' + self.weapon
        
class unconscious(models.Model):
    unit = models.ForeignKey(md.NewUser, on_delete=models.CASCADE)
    state = models.BooleanField()
    createdat = models.DateTimeField()
    updateat = models.DateTimeField()
    
    def __str__(self):
        return self.unit + ' ' + self.state

class kills(models.Model):
    killer = models.ForeignKey(md.NewUser, on_delete=models.CASCADE)
    #killer = models.TextField(default=0)
    weapon= models.TextField(default=0)
    killed= models.TextField(default=0)
    distance= models.TextField(default=0)
    createdat = models.DateTimeField()
    updateat = models.DateTimeField()
    
    def __str__(self):
        return self.killer + ' ' + self.weapon

class medic(models.Model):
    healer = models.ForeignKey(md.NewUser, on_delete=models.CASCADE)
    #healer = models.BooleanField()
    healed= models.TextField()
    hitLocation= models.TextField()
    typeOfHeal= models.TextField()
    createdat = models.DateTimeField()
    updateat = models.DateTimeField()
    
    def __str__(self):
        return self.healer + ' ' + self.typeOfHeal