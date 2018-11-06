from django.db import models
from django.contrib.auth.models import User



class Document(models.Model):
    file = models.FileField(upload_to='documents/')


# class UserLogin(models.Model):
#     user = models.OneToOneField(User, True)

#     def __str__(self):
#         return self.user.name
