from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    steamID = models.BigIntegerField(unique=True)
    vestName = models.CharField(max_length=150,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name','steamID','vestName']

    def __str__(self):
        return self.user_name