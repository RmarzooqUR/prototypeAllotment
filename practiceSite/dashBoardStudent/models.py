from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class UserLogin(User):
    # user = models.OneToOneField(User,True)
    # username = models.CharField(max_length = 120, default = 'username')
    # user = models.ManyToOneRel(User, True, "student user")
    isStudent = models.BooleanField(default=False)
    isProvost = models.BooleanField(default=False)

    def __str__(self):
        return self.username
