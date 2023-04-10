from django.db import models

from django.contrib.auth.models import AbstractUser
#Thêm avatar cho user
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=255,blank=True,null=True)