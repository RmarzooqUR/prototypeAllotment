from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentLogin(models.Model):

	student_user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username
