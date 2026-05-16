from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
 email = models.EmailField(unique=True, blank=False, null= False)

class Profile(models.Model): 
 user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 phone_number = models.CharField(max_length = 15)
  
 def __str__(self):
  return self.user.username
 