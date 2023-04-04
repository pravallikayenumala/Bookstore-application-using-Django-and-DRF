from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    country_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, unique=False)
    otp = models.CharField(max_length=6)
    location = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    #groups = models.ManyToManyField(verbose_name=('groups'), blank=True, related_name='auth_user_groups')


    


