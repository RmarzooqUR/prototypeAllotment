from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserLogin(models.Model):
    user = models.OneToOneField(User,True)
    
    def __str__(self):
        return self.user.name
